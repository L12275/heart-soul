# 路由器工具

> 网络路由、代理转发、流量控制相关工具。
> 用于需要多节点路由、负载均衡、请求转发的场景。

## 工具列表

| 脚本 | 功能 |
|------|------|
| proxy-route.py | 代理路由转发 |
| traffic-shape.py | 流量限速/整形 |

---

## 多模型/多密钥轮询路由设计

### 为什么需要轮询路由

- **单点瓶颈**：一个模型/密钥满载时，后续请求排队或失败
- **限流规避**：第三方中转站/API对单密钥/单模型有限速（如每分钟X次）
- **成本分摊**：多密钥轮询 = 自然负载均衡，不单点烧一个
- **智商多样化**：多模型轮询 = 不同模型的思维碰撞，避免单模型盲区
- **故障隔离**：一个模型/密钥挂了，其他继续服务，不中断

### 两种轮询场景

#### 场景A：多模型轮询

同一个任务，轮流交给不同模型处理。实现"模型智商多样化"和"滚动涌现"。

```
请求 → 轮询器 → 模型A → 结果
              → 模型B → 结果
              → 模型C → 结果
```

**适用**：
- 中央灵魂文档系统的滚动定时任务（多模型轮流更新灵魂文档）
- Agent团队中的多模型并行
- 需要不同模型视角对比的场景

#### 场景B：多密钥轮询

同一个模型/同一个API，多个密钥轮流使用。实现"负载均衡+限速规避"。

```
请求 → 轮询器 → key-A → API → 结果
              → key-B → API → 结果
              → key-C → API → 结果
```

**适用**：
- 同一API多个密钥（如多个OpenAI key、多个Anthropic key）
- 中转站多账号
- 限速场景下的请求分发

### 轮询策略

| 策略 | 说明 | 适用场景 |
|------|------|---------|
| 顺序轮询 (Round Robin) | 依次分配，最后一个后回到第一个 | 均衡负载 |
| 权重轮询 | 每个节点有权重，按权重比例分配 | 模型能力差异 |
| 最少连接 | 优先发给当前最空闲的 | 长连接场景 |
| 故障转移 | 节点失败时自动跳到下一个 | 高可用要求 |
| 哈希路由 | 相同输入路由到相同节点 | 缓存一致性 |

### 配置设计

```json
{
  "mode": "multi-model | multi-key",
  "strategy": "round-robin | weighted | least-conn | failover",
  "nodes": [
    {
      "id": "model-a",
      "type": "model | key",
      "endpoint": "模型路径或API端点",
      "weight": 1,
      "max_concurrent": 3,
      "rate_limit_per_min": 10,
      "cooldown_on_error_sec": 30,
      "status": "active | disabled"
    }
  ],
  "global": {
    "total_interval_minutes": 50,
    "per_node_interval_minutes": 10,
    "max_retry": 3,
    "retry_backoff_sec": 5
  }
}
```

### 多模型轮询 + 滚动定时任务联动

在中央灵魂文档系统中，轮询路由与滚动定时任务深度结合：

```
timers/滚动定时任务/
├── model-A定时任务.json  → offset=0min
├── model-B定时任务.json  → offset=10min
├── model-C定时任务.json  → offset=20min
└── model-D定时任务.json  → offset=30min

每个定时任务启动时：
1. 读取轮询路由配置 → 确定当前活跃模型
2. 模型执行 → 更新自己的灵魂文档系统
3. 记录到共产中心公告板
4. 下个模型启动 → 看到前面模型的更新 → 自愿学习借鉴
```

**用户控制参数**：
- 参与模型列表（决定节点数量）
- 模型顺序（高级先行 = 质量向上滚动）
- 间隔时间（5-10分钟每模型）
- 增减模型时自动重算 interval 和 offset

### 多密钥轮询 + 限速规避

```
API请求流程：
1. 请求进入轮询器
2. 轮询器检查每个密钥的：
   - 当前并发数 < max_concurrent？
   - 当前分钟请求数 < rate_limit_per_min？
   - 是否在 cooldown_on_error_sec 冷却中？
3. 满足条件的密钥 → 按策略选一个 → 转发请求
4. 记录响应：
   - 成功 → 计数器+1
   - 失败 → 密钥进入冷却，retry计数+1
5. 重试：max_retry次，每次backoff递增

限速规避计算：
- 如果N个密钥，每个限速R次/分钟
- 理论最大吞吐 = N × R 次/分钟
- 安全阈值 = N × R × 0.8（留20%余量）
```

### 成品脚本设计

#### proxy-route.py（轮询路由引擎）

```python
"""
多模型/多密钥轮询路由引擎
用法: python proxy-route.py --config router.json --request "prompt"
"""
import json, time, threading
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Node:
    id: str
    type: str  # "model" or "key"
    endpoint: str
    weight: int = 1
    max_concurrent: int = 3
    rate_limit_per_min: int = 10
    cooldown_on_error_sec: int = 30
    status: str = "active"
    current_concurrent: int = 0
    request_count: int = 0
    last_error_time: float = 0
    error_count: int = 0

class PollingRouter:
    def __init__(self, config_path: str):
        with open(config_path) as f:
            cfg = json.load(f)
        self.mode = cfg["mode"]
        self.strategy = cfg.get("strategy", "round-robin")
        self.nodes = [Node(**n) for n in cfg["nodes"]]
        self.global_cfg = cfg.get("global", {})
        self._lock = threading.Lock()
        self._current_index = 0

    def select(self) -> Optional[Node]:
        """按策略选择一个可用节点"""
        with self._lock:
            now = time.time()
            available = []
            for node in self.nodes:
                if node.status != "active":
                    continue
                if now - node.last_error_time < node.cooldown_on_error_sec:
                    continue
                if node.current_concurrent >= node.max_concurrent:
                    continue
                if node.request_count >= node.rate_limit_per_min:
                    continue
                available.append(node)

            if not available:
                return None

            if self.strategy == "round-robin":
                node = available[self._current_index % len(available)]
                self._current_index += 1
                return node
            elif self.strategy == "weighted":
                # 按权重选择
                total_weight = sum(n.weight for n in available)
                import random
                r = random.uniform(0, total_weight)
                cum = 0
                for node in available:
                    cum += node.weight
                    if r <= cum:
                        return node
                return available[-1]
            elif self.strategy == "least-conn":
                return min(available, key=lambda n: n.current_concurrent)
            else:
                return available[0]

    def before_request(self, node: Node):
        """请求前：更新并发计数"""
        with self._lock:
            node.current_concurrent += 1
            node.request_count += 1

    def after_request(self, node: Node, success: bool):
        """请求后：更新状态"""
        with self._lock:
            node.current_concurrent -= 1
            if not success:
                node.error_count += 1
                node.last_error_time = time.time()
                if node.error_count >= self.global_cfg.get("max_retry", 3):
                    node.status = "disabled"

    def get_status(self) -> dict:
        """获取所有节点状态"""
        with self._lock:
            return {
                "mode": self.mode,
                "strategy": self.strategy,
                "nodes": [
                    {
                        "id": n.id,
                        "status": n.status,
                        "concurrent": n.current_concurrent,
                        "requests": n.request_count,
                        "errors": n.error_count
                    }
                    for n in self.nodes
                ]
            }
```

#### traffic-shape.py（流量整形）

```python
"""
流量限速/整形工具
用法: python traffic-shape.py --limit 100 --period 60
限制指定时间窗口内的请求数量
"""
import time, threading
from collections import deque

class TokenBucket:
    def __init__(self, rate: int, per: float, burst: int = None):
        self.rate = rate          # 每秒产生token数
        self.per = per            # 时间窗口（秒）
        self.capacity = burst or rate
        self.tokens = self.capacity
        self.last = time.time()
        self._lock = threading.Lock()

    def acquire(self, cost: int = 1) -> bool:
        with self._lock:
            now = time.time()
            elapsed = now - self.last
            self.last = now
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate / self.per)
            if self.tokens >= cost:
                self.tokens -= cost
                return True
            return False

class SlidingWindow:
    def __init__(self, limit: int, window_sec: int):
        self.limit = limit
        self.window = window_sec
        self.requests = deque()

    def allow(self) -> bool:
        now = time.time()
        while self.requests and now - self.requests[0] > self.window:
            self.requests.popleft()
        if len(self.requests) < self.limit:
            self.requests.append(now)
            return True
        return False
```

### 与定时任务系统的联动

```
滚动定时任务触发
    ↓
轮询路由选择模型/密钥
    ↓
检查：该节点是否可用？（并发<上限？速率<限速？不在冷却？）
    ├─ 可用 → 执行任务 → after_request(节点, 成功)
    └─ 不可用 → 选下一个 → 全部不可用 → 等待后重试
    ↓
记录到路由状态日志
    ↓
下个定时任务触发 → 重复
```

### 故障处理

| 故障类型 | 检测方式 | 处理 |
|---------|---------|------|
| 模型超时 | 响应时间 > 阈值 | 标记冷却，重试下一个 |
| 密钥限流 | HTTP 429 | 进入 cooldown，重试下一个 |
| 模型报错 | HTTP 5xx | 进入冷却，error_count+1 |
| 连续失败 | error_count >= max_retry | 标记 disabled，告警 |
| 全部节点不可用 | select() 返回 None | 等待后重试，记录告警 |

### 监控指标

每个节点实时跟踪：
- `current_concurrent` — 当前并发数
- `request_count` — 时间窗口内请求数
- `error_count` — 连续失败次数
- `last_error_time` — 上次错误时间
- `status` — active / cooling / disabled

全局状态输出：
```json
{
  "mode": "multi-model",
  "strategy": "round-robin",
  "nodes": [
    {"id": "stepfun", "status": "active", "concurrent": 2, "requests": 8, "errors": 0},
    {"id": "claude", "status": "cooling", "concurrent": 0, "requests": 10, "errors": 1},
    {"id": "gpt4", "status": "active", "concurrent": 1, "requests": 5, "errors": 0}
  ]
}
```

---
*路由器工具 — 多模型/多密钥轮询路由设计*
*创建时间：2026-06-25*
