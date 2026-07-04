# 每日商业情报简报: 2026-07-04


**日期:** 2026-07-04
**生成时间:** 01:19
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [Giant trees have no trouble pumping water to top branches](https://news.exeter.ac.uk/faculty-of-environment-science-and-economy/giant-trees-have-no-trouble-pumping-water-to-top-branches/)
📍 Hacker News | 🔥 73 points | 🕒 2 hours ago

### 2. [Leanstral 1.5: Proof Abundance for All](https://mistral.ai/news/leanstral-1-5/)
📍 Hacker News | 🔥 64 points | 🕒 2 hours ago

### 3. [Soatok's Informal Guide to Threat Models](https://soatok.blog/2026/06/30/soatoks-informal-guide-to-threat-models/)
📍 Hacker News | 🔥 18 points | 🕒 41 minutes ago

### 4. [Steam Controller Auto-Charge – pilot to magnetic charging puck using CV](https://github.com/FossPrime/Steam-Controller-Auto-Charge)
📍 Hacker News | 🔥 56 points | 🕒 2 hours ago

### 5. [SearXNG: A free internet metasearch engine](https://github.com/searxng/searxng)
📍 Hacker News | 🔥 126 points | 🕒 5 hours ago

### 6. [MSI Center – How to gain SYSTEM privileges in seconds](https://mrbruh.com/msicenter/)
📍 Hacker News | 🔥 7 points | 🕒 19 minutes ago

### 7. [GLM5.2 on AMD MI355X at 2626 tok/s/node at over 2x lower cost than Blackwell](https://www.wafer.ai/blog/glm52-amd)
📍 Hacker News | 🔥 70 points | 🕒 3 hours ago

### 8. [The circuit that lets your brain think and see](https://www.engineering.columbia.edu/about/news/circuit-lets-your-brain-think-and-see)
📍 Hacker News | 🔥 25 points | 🕒 2 hours ago

### 9. [Amsterdam invented the fire department](https://worksinprogress.co/issue/how-amsterdam-invented-the-fire-department/)
📍 Hacker News | 🔥 32 points | 🕒 2 hours ago

### 10. [What does privatization of the US Postal Service mean?](https://phenomenalworld.org/analysis/unstitching-america/)
📍 Hacker News | 🔥 15 points | 🕒 1 hour ago

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [特斯拉、Meta到Anthropic，三星电子的芯片代工订单积压已达50万亿韩元](https://wallstreetcn.com/articles/3776186)
📍 WallStreetCN | 🕒 01:08

### 2. [美股现3个月最大资金流出，而日股迎来7周最大资金流入](https://wallstreetcn.com/articles/3776188)
📍 WallStreetCN | 🕒 01:07

### 3. [电子商务法修正草案公开征求意见](https://wallstreetcn.com/livenews/3128867)
📍 WallStreetCN | 🕒 01:01

### 4. [SemiAnalysis：在英伟达系统中的内存支出占比到2026年底将超过30%，并在2027年超过40%](https://wallstreetcn.com/livenews/3128855)
📍 WallStreetCN | 🕒 00:36

### 5. [芯片股跌倒，黄金、比特币齐欢庆](https://wallstreetcn.com/charts/41959349)
📍 WallStreetCN | 🕒 00:02

### 6. [华尔街见闻早餐FM-Radio | 2026年7月4日](https://wallstreetcn.com/articles/3776185)
📍 WallStreetCN | 🕒 23:18

### 7. [AI焦虑暂退，科技股反弹，欧股两日连创新高，布油两日反弹但连跌四周](https://wallstreetcn.com/articles/3776124)
📍 WallStreetCN | 🕒 23:00

### 8. [数据中心电价飙升60倍！美国最大电网启动二级紧急警报，北弗吉尼亚电价突破2500美元/MWh](https://wallstreetcn.com/articles/3776184)
📍 WallStreetCN | 🕒 22:06

### 9. [智利锂矿巨头计划扩产70%！Novandino将锂年产目标设定最高47万吨](https://wallstreetcn.com/articles/3776182)
📍 WallStreetCN | 🕒 21:27

### 10. [俄总统新闻秘书：普京宣布俄军“完全解放”卢甘斯克](https://wallstreetcn.com/articles/3776183)
📍 WallStreetCN | 🕒 20:50

## 📚 学术前沿 (Research)
> ArXiv AI/ML Papers

### 1. [Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514v1)
> ⚡ As AI coding agents become more autonomous, they increasingly ship code iterativ...
👤 Josh Hills, Ida Caspary | 📅 2026-07-02

**详情:** As AI coding agents become more autonomous, they increasingly ship code iteratively, with the codebase persisting across sessions. This persistence creates a new attack surface: a misaligned or prompt-injected agent can distribute attacks across pull requests (PRs) and time its payload for the PR with the best natural cover. To study the resulting dynamics, we introduce Iterative VibeCoding, a setting for AI control, the study of safely deploying capable but potentially untrusted AI. In Iterative VibeCoding, a coding agent builds software over a sequence of PRs in a persistent codebase while pursuing a covert side task. Our benchmark includes two task families: CLI tools and Flask web services, across 20 total task variations. We use Claude Sonnet 4.5 as the attack agent and GPT-4o as the monitor. We compare gradual attacks, which distribute the side task across PRs, against non-gradual attacks concentrated in a single PR. No single monitor is robust to both: which strategy evades best (success while evading the monitor) depends on the monitor type, so a defender cannot close off both gradual and non-gradual attacks with any one monitor. High evasion (&gt;= 65%) generalizes across model attack agent backends (Sonnet 4.5, Gemini 3.1 Pro, Kimi K2.5), confirming this is a property of the persistent-state attack surface rather than a single model's capability. Evasion also remains high across state-of-the-art monitor models and the gap between gradual and non-gradual evasion widens for more capable models. We introduce a stateful link-tracker monitor that tracks suspicious buildup across PRs. On both task families, it detects gradual attacks substantially better than diff monitors that merely see more accumulated history. Combining this stronger monitor with trajectory monitors in a four-monitor ensemble reduces gradual-attack evasion from 93% under the weakest standard diff monitor to 47%.

### 2. [LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning](https://arxiv.org/abs/2607.02513v1)
> ⚡ LLMs memorize sensitive training data, including personally identifiable informa...
👤 Matteo Boglioni, Thibault Rousset | 📅 2026-07-02

**详情:** LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's parameters or merely obfuscates it, a concern reinforced by the success of resurfacing attacks. To bridge this gap, we introduce LACUNA: the first unlearning testbed with ground-truth parameter-level localization. LACUNA injects PII of synthetic individuals into predefined parameters of 1B and 7B OLMo-based models via masked continual pretraining, enabling direct evaluation of whether unlearning targets the weights responsible for knowledge storage. We use LACUNA to benchmark current SOTA unlearning methods and find that, despite strong output-level performance, existing methods are highly imprecise and susceptible to resurfacing attacks. We further show that when localization is successful, even a simple gradient-based unlearning method achieves strong erasure and robustness to resurfacing attacks, highlighting the importance of precise unlearning. We release LACUNA to complement behavioral evaluations and drive further advances in robust, localization-based unlearning.

### 3. [Program-as-Weights: A Programming Paradigm for Fuzzy Functions](https://arxiv.org/abs/2607.02512v1)
> ⚡ Many everyday programming tasks resist clean rule-based implementation, such as ...
👤 Wentao Zhang, Liliana Hotsko | 📅 2026-07-02

**详情:** Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (PAW), in which a 4B compiler trained on FuzzyBench, a 10M-example dataset we release, emits parameter-efficient adapters for a frozen, lightweight interpreter. A 0.6B Qwen3 interpreter executing PAW programs matches the performance of direct prompting of Qwen3-32B, while using roughly one fiftieth of the inference memory and running at 30 tokens/s on a MacBook M3. PAW reframes the foundation model from a per-input problem solver into a tool builder: invoked once per function definition, it produces a small reusable artifact whose subsequent calls per function application are cheap and offline.

### 4. [Online Safety Monitoring for LLMs](https://arxiv.org/abs/2607.02510v1)
> ⚡ Despite alignment training, LLMs remain prone to generating unsafe outputs at de...
👤 Mona Schirmer, Metod Jazbec | 📅 2026-07-02

**详情:** Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with more advanced monitors based on sequential hypothesis testing.

### 5. [ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509v1)
> ⚡ Understanding and reasoning over long contexts has become a key requirement for ...
👤 Yanjun Zhao, Ruizhong Qiu | 📅 2026-07-02

**详情:** Understanding and reasoning over long contexts has become a key requirement for deploying large language models (LLMs) in realistic applications. Although recent LLMs support increasingly long context windows, they often fail to use relevant evidence that is already present in the input, revealing a gap between context access and effective context utilization. In this work, we propose Recursive Evidence Replay as LLM Harness for Long-Context Reasoning (RECONTEXT), a training-free inference method for improving long-context reasoning. RECONTEXT uses model-internal relevance signals to construct a query-conditioned evidence pool and replays it before final generation while preserving the full original context. This recursive selection process separates evidence organization from answer generation without training, external memory, or context pruning. We also provide a theoretical analysis based on associative memory, which characterizes the context as a memory store, the question as a retrieval cue, attention as cue-trace association, and replay as trace reactivation. Experiments on eight long-context datasets with 128K context length show that RECONTEXT consistently improves evidence utilization across Qwen3-4B, Qwen3-8B, and Llama3-8B, achieving the best average rank on all three backbones. Code is available at https://github.com/Yanjun-Zhao/ReContext.

## 💎 产品精选 (Product Gems)
> Product Hunt Today

### 1. [Upstream](https://www.producthunt.com/posts/upstream-5)
> The inbox designed for humans and agents
🔥 928 votes

### 2. [Goldfish](https://www.producthunt.com/posts/goldfish)
> Press Option. It knows your work and replies like you
🔥 922 votes

### 3. [Tencent EdgeOne Makers](https://www.producthunt.com/posts/tencent-edgeone-makers)
> Ship AI agents like web apps, in minutes.
🔥 874 votes

### 4. [Context.dev](https://www.producthunt.com/posts/context-dev-2)
> One API to scrape, enrich, and extract the internet
🔥 826 votes

### 5. [Acti](https://www.producthunt.com/posts/acti-3)
> Agentic keyboard for mobile commands and search
🔥 789 votes

### 6. [Bond](https://www.producthunt.com/posts/bond-717)
> The AI to-do list that does itself
🔥 775 votes

### 7. [Mailwarm 2.0](https://www.producthunt.com/posts/mailwarm-2-0)
> The email warmup tool, upgraded for deliverability.
🔥 710 votes

### 8. [Fypro](https://www.producthunt.com/posts/fypro)
> Convert your TikTok followers into paying customers
🔥 708 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [家里亲戚今年高考，求推荐本科专业](https://www.v2ex.com/t/1224690)
💬 150 replies

### 2. [“有个东西，也是我今天才学到的，叫 CDN”](https://www.v2ex.com/t/1224709)
💬 127 replies

### 3. [[OneDayAI] 先送后卖，新老用户留言即送一周套餐，每 20 楼抽 20 刀充值额度](https://www.v2ex.com/t/1224726)
💬 92 replies

### 4. [看《感觉女友很爱去看演唱会，不想让她去怎么办》有感，人生真正的享受是什么](https://www.v2ex.com/t/1224760)
💬 79 replies

### 5. [我预判，第一波 AI 洪峰已过！](https://www.v2ex.com/t/1224778)
💬 68 replies

## 📕 小红书雷达 (XHS Radar)
> 手动搜索指令 (点击链接进入搜索页)

### 1. [🔎 搜索指令: 毕设求助](https://www.xiaohongshu.com/search_result?keyword=毕设求助&source=web_search_result_notes)
> 点击查找关于 '毕设求助' 的帖子。重点关注标签: 救命, 有偿, 急, 我要疯了, 红包, 太难了, 求教。...

### 2. [🔎 搜索指令: python代做](https://www.xiaohongshu.com/search_result?keyword=python代做&source=web_search_result_notes)
> 点击查找关于 'python代做' 的帖子。重点关注标签: 救命, 有偿, 急, 我要疯了, 红包, 太难了, 求教。...

### 3. [🔎 搜索指令: 数据分析 救命](https://www.xiaohongshu.com/search_result?keyword=数据分析%20救命&source=web_search_result_notes)
> 点击查找关于 '数据分析 救命' 的帖子。重点关注标签: 救命, 有偿, 急, 我要疯了, 红包, 太难了, 求教。...

### 4. [🔎 搜索指令: 竞品分析 工具](https://www.xiaohongshu.com/search_result?keyword=竞品分析%20工具&source=web_search_result_notes)
> 点击查找关于 '竞品分析 工具' 的帖子。重点关注标签: 救命, 有偿, 急, 我要疯了, 红包, 太难了, 求教。...

### 5. [🔎 搜索指令: 批量 采集 小红书](https://www.xiaohongshu.com/search_result?keyword=批量%20采集%20小红书&source=web_search_result_notes)
> 点击查找关于 '批量 采集 小红书' 的帖子。重点关注标签: 救命, 有偿, 急, 我要疯了, 红包, 太难了, 求教。...

### 6. [🔎 搜索指令: 自动回复 脚本](https://www.xiaohongshu.com/search_result?keyword=自动回复%20脚本&source=web_search_result_notes)
> 点击查找关于 '自动回复 脚本' 的帖子。重点关注标签: 救命, 有偿, 急, 我要疯了, 红包, 太难了, 求教。...

## 💡 深度洞察 (Insights)
> HN Top Blogs - 精选技术博客

### 1. [Quickly apply LUTs (color grading) with ffmpeg](https://www.jeffgeerling.com/blog/2026/apply-lut-color-grade-with-ffmpeg/)
📍 jeffgeerling.com | 📅 Thu, 25 Jun 2026

### 2. [Framework's 10G Ethernet module exposes USB-C's complexity](https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/)
📍 jeffgeerling.com | 📅 Wed, 24 Jun 2026

### 3. [Text AI watermarks will always be trivial to remove](https://seangoedecke.com/text-ai-watermarks/)
📍 seangoedecke.com | 📅 Thu, 02 Jul 2026

### 4. [Saying the obvious thing](https://seangoedecke.com/saying-the-obvious-thing/)
📍 seangoedecke.com | 📅 Sat, 27 Jun 2026

### 5. [FBI Seizes NetNut Proxy Platform, Popa Botnet](https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/)
📍 krebsonsecurity.com | 📅 Thu, 02 Jul 2026

---
*报告由 Unified Intelligence Engine V2 自动生成*