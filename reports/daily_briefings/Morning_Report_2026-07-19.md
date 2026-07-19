# 每日商业情报简报: 2026-07-19


**日期:** 2026-07-19
**生成时间:** 01:11
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [Speech Recognition and TTS in less than 500kb](https://github.com/moonshine-ai/moonshine/tree/main/micro)
📍 Hacker News | 🔥 248 points | 🕒 5 hours ago

### 2. [Classic Amiga titles, free to download](https://amigafreeware.downer.tech/)
📍 Hacker News | 🔥 43 points | 🕒 3 hours ago

### 3. [GPT-5.6 used a prompt to close a 30-year gap in convex optimization](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/)
📍 Hacker News | 🔥 491 points | 🕒 12 hours ago

### 4. [If You Build It, They Will Come](https://www.benlandautaylor.com/p/if-you-build-it-they-will-come)
📍 Hacker News | 🔥 263 points | 🕒 9 hours ago

### 5. [Mayor Mamdani Says Landlords Can't Use AI Images to Advertise](https://petapixel.com/2026/07/16/mayor-mamdani-says-landlords-cant-secretly-use-ai-images-to-advertise-properties/)
📍 Hacker News | 🔥 165 points | 🕒 2 hours ago

### 6. [Judge a book by its first pages](https://uncovered.ink)
📍 Hacker News | 🔥 38 points | 🕒 3 hours ago

### 7. [Real-Time LuaTeX: Recompiling Large Documents in 1ms [pdf]](https://www.tug.org/tug2026/preprints/lode-realtime.pdf)
📍 Hacker News | 🔥 25 points | 🕒 3 hours ago

### 8. [I'm Making Strandfall, a Solarpunk Orienteering Larp](https://mssv.net/2026/04/29/im-making-strandfall-a-solarpunk-orienteering-larp/)
📍 Hacker News | 🔥 89 points | 🕒 6 hours ago

### 9. [Hardcore IndieWeb: Run your own website 100% independently for only $0.01/day](https://www.neatnik.net/hardcore-indieweb)
📍 Hacker News | 🔥 65 points | 🕒 3 hours ago

### 10. [Gleam Is Now on Tangled](https://tangled.org/gleam.run/gleam)
📍 Hacker News | 🔥 203 points | 🕒 9 hours ago

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [美官员称“约旦美军基地5天遭4袭，美军两人死亡”，伊朗最高领袖强调将给美国留下“刻骨铭心的教训”](https://wallstreetcn.com/articles/3777329)
📍 WallStreetCN | 🕒 00:42

### 2. [美国中央司令部：2名美军士兵在约旦因伊朗袭击而死亡，另有1人失踪](https://wallstreetcn.com/livenews/3136082)
📍 WallStreetCN | 🕒 17:16

### 3. [印尼投资部部长：对中印尼投资合作未来充满信心](https://wallstreetcn.com/livenews/3136080)
📍 WallStreetCN | 🕒 17:13

### 4. [伊朗最高领袖：美国行为证明其总统签字“毫无价值”](https://wallstreetcn.com/livenews/3136073)
📍 WallStreetCN | 🕒 16:36

### 5. [AI手机告别功能竞赛，荣耀开始重构操作系统](https://wallstreetcn.com/articles/3777328)
📍 WallStreetCN | 🕒 15:43

### 6. [伊朗外交部：谅解备忘录不允许美在霍尔木兹海峡开辟独立平行航线](https://wallstreetcn.com/livenews/3136065)
📍 WallStreetCN | 🕒 15:24

### 7. [王毅：赞赏印尼方重申欢迎中资企业赴印尼投资合作](https://wallstreetcn.com/livenews/3136058)
📍 WallStreetCN | 🕒 14:37

### 8. [蔚来芯片子公司神玑首次独立参展WAIC，瞄准汽车之外AI市场](https://wallstreetcn.com/articles/3777326)
📍 WallStreetCN | 🕒 14:01

### 9. [天孚通信：预计2026年上半年净利润同比增长25.00%-45.00%](https://wallstreetcn.com/livenews/3136043)
📍 WallStreetCN | 🕒 13:19

### 10. [伊朗副外长：伊朗已停止履行伊美谅解备忘录](https://wallstreetcn.com/livenews/3136030)
📍 WallStreetCN | 🕒 12:33

## 📚 学术前沿 (Research)
> ArXiv AI/ML Papers

### 1. [RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275v1)
> ⚡ Recent robot foundation models operate with single-step or short-history visuomo...
👤 Yunfan Jiang, Yevgen Chebotar | 📅 2026-07-16

**详情:** Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new robot capabilities: one-shot in-context imitation from human video demonstrations, on-the-fly policy improvement, robustness to perturbations, and stronger performance on multi-stage, long-horizon tasks. We also observe, for the first time, steady gains in closed-loop performance as pretraining context length scales. At its core, RoboTTT integrates Test-Time Training into robot foundation models such as Vision-Language-Action policies, yielding a sequence model whose recurrent state consists of fast weights, parameters updated by gradient descent during both training and inference, compressing histories into weight space and retrieving contextual information for long-context conditioning. To scale training context length, the recipe combines sequence action forcing with truncated backpropagation through time. On challenging real-robot manipulation tasks, RoboTTT improves overall performance by 87% over the single-step context baseline and fully completes a five-minute, ten-stage assembly task, which no baseline ever does. RoboTTT trained with 8K-timestep context outperforms the same model pretrained with 1K timesteps by 62%, suggesting context length as a new scaling axis for robot foundation models. Videos are available at https://research.nvidia.com/labs/gear/robottt/

### 2. [SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions](https://arxiv.org/abs/2607.15272v1)
> ⚡ Editing the figures in a research paper is a routine and time-consuming part of ...
👤 Yasheng Sun, Zezi Zeng | 📅 2026-07-16

**详情:** Editing the figures in a research paper is a routine and time-consuming part of everyday research practice: authors relabel components, rearrange panels, and restyle visuals as they revise their manuscripts. Automating this editing workflow under a natural-language instruction, however, is challenging, because a scientific figure is a dense infographic in which heterogeneous visual elements such as schematics, plots, photos, captions, and arrows are composed under a tight visual grammar to advance a specific argument. To address this, we present SciDiagramEdit, a benchmark and skill-evolution framework that learns from natural paper revisions and operates on the figure's editable vector source, where users can inspect and co-edit individual primitives alongside the agent. Our benchmark mines before/after figure pairs from arXiv version histories, each grounded in the authors' own revision intent. To accommodate the diversity of editing instructions, we adopt agentic learning via skill evolution: an agentic proposer continually refines the agent's skill specification from execution traces over multiple epochs. The resulting skill progressively lifts edit accuracy on a held-out validation set, providing evidence that natural paper revisions are an effective training signal for instruction-driven figure editing.

### 3. [Pretraining Data Can Be Poisoned through Computational Propaganda](https://arxiv.org/abs/2607.15267v1)
> ⚡ Poisoning pretraining data can introduce harmful behaviors to LMs that are diffi...
👤 Victoria Graf, Hannaneh Hajishirzi | 📅 2026-07-16

**详情:** Poisoning pretraining data can introduce harmful behaviors to LMs that are difficult to detect and mitigate. Prior work on poisoning pretraining data has largely exploited established data sources such as Wikipedia, which do not represent the large scale and heterogeneity typical of pretraining corpora, and has ignored the interaction between poisoned data and data curation pipelines. We demonstrate that poisoning attacks on pretraining data are feasible beyond this limited setting through an existing web-scale content injection mechanism: public discussion interfaces. Additionally, to measure whether malicious content is included after web crawling and data curation, we introduce HalfLife, a novel analysis for estimating adversarial content inclusion in web-crawl based LM training data. We use HalfLife to explore the feasibility of poisoning pretraining corpora at web scale through open discussion interfaces. Our analysis demonstrates the importance of estimating whether poison injections are included in pretraining data, and establishes third-party webpage content as a possible vector for attacking language model pretraining.

### 4. [SceneBind: Binding What and Where Across Vision, Audio and Language](https://arxiv.org/abs/2607.15265v1)
> ⚡ We present SceneBind, an omni-modal representation of realistic scenes with join...
👤 Mingfei Chen, Zijun Cui | 📅 2026-07-16

**详情:** We present SceneBind, an omni-modal representation of realistic scenes with joint semantic and 3D spatial understanding across vision, audio and language. Existing omni-modal encoders excel at instance-level semantics (i.e., what is present), but often lack explicit spatial structure (i.e., where it is). SceneBind addresses this gap by representing each scene as a semantic-spatial entity, combining a global semantic embedding with object-centric semantic-spatial slots. This representation explicitly captures object-level semantics, spatial attributes, and uncertainty. We further propose SceneBind Matching, a semantic-spatial matching scheme that integrates global scene similarity with object alignment, supporting cross-modal scene retrieval and object grounding. To train and evaluate SceneBind, we curate a novel real-world binaural audio-visual dataset with structured semantic and spatial annotations, and propose a training protocol for aligning semantic and spatial signals across modalities. SceneBind is compatible with large-scale pretrained semantic encoders, adds lightweight spatial modeling with only a few additional tokens. It achieves state-of-the-art scene and spatial retrieval while enabling strong zero-shot transfer to downstream tasks such as audio-visual localization.

### 5. [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263v1)
> ⚡ Security-agent evaluations commonly measure peak offensive capability under gene...
👤 Paul Kassianik, Blaine Nelson | 📅 2026-07-16

**详情:** Security-agent evaluations commonly measure peak offensive capability under generous inference budgets, emphasizing vulnerability discovery, exploit development, penetration testing, and CTF completion. Such measurements are useful but incomplete: in operational security, every reasoning step, tool call, telemetry query, and enrichment request consumes budget. We evaluate language-model security agents through this cost-success lens on offensive Cybench challenges and defensive Splunk BOTS v1 investigation challenges. Instead of reporting only best-case success, we compare models at fixed cost levels and decompose performance by inference spend and tool spend. Our results show distinct scalingregimes for red- and blue-team tasks. Offensive CTF performance improves with additional test-time compute, and scaled open-weight models can approach frontier proprietary systems while remaining cost-competitive. Defensive SOC investigation does not scale in the same way: success depends more heavily on disciplined tool use, telemetry navigation, and selective enrichment than on raw reasoning budget alone. We argue that security-agent benchmarks should measure economic efficiency and operational fit alongside task success. Cost-aware, SOC-native evaluations provide a clearer picture of which models are practically useful today and where defensive agents still need to improve. We present an interactive website with our results https://evals.frontier.security.

## 💎 产品精选 (Product Gems)
> Product Hunt Today

### 1. [Acti](https://www.producthunt.com/posts/acti-3)
> Agentic keyboard for mobile commands and search
🔥 1497 votes

### 2. [Tencent EdgeOne Makers](https://www.producthunt.com/posts/tencent-edgeone-makers)
> Ship AI agents like web apps, in minutes.
🔥 1219 votes

### 3. [Context.dev](https://www.producthunt.com/posts/context-dev-2)
> One API to scrape, enrich, and extract the internet
🔥 1187 votes

### 4. [AnySearch](https://www.producthunt.com/posts/anysearch-3)
> Real-time structured search trusted by agents and developers
🔥 950 votes

### 5. [ExploreYC](https://www.producthunt.com/posts/exploreyc-2)
> Open-source API for Y Combinator & a16z company data
🔥 904 votes

### 6. [ClawTeams](https://www.producthunt.com/posts/clawteams-a263d5d3-d341-45d9-9e9f-7154e7066e4a)
> The first goal-driven, proactive AI team for e-commerce
🔥 870 votes

### 7. [Pazi](https://www.producthunt.com/posts/pazi-2)
> Vibe code business operations
🔥 832 votes

### 8. [ChatCut](https://www.producthunt.com/posts/chatcut-2)
> Your AI video editor in ChatGPT, desktop, and web
🔥 815 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [纯功利的角度, 如何为孩子选兴趣班？](https://www.v2ex.com/t/1228170)
💬 111 replies

### 2. [假如没有厕纸了，你用什么？](https://www.v2ex.com/t/1228159)
💬 76 replies

### 3. [投资建议：自有宅基地建房出租。](https://www.v2ex.com/t/1228206)
💬 47 replies

### 4. [裁员 n+1，已签解除合同，社保和公积金还能要求公司补吗？](https://www.v2ex.com/t/1228195)
💬 42 replies

### 5. [大家用 AI 写代码真实感受是啥？](https://www.v2ex.com/t/1228212)
💬 40 replies

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

### 1. [QuadRF can spot drones and see WiFi through my wall](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/)
📍 jeffgeerling.com | 📅 Fri, 10 Jul 2026

### 2. [The Special Value Pi 4 was extremely short-lived](https://www.jeffgeerling.com/blog/2026/special-value-pi-4-extremely-short-lived/)
📍 jeffgeerling.com | 📅 Wed, 08 Jul 2026

### 3. [Overtraining as the path to human-like AI](https://seangoedecke.com/overtraining-as-the-path-to-human-like-ai/)
📍 seangoedecke.com | 📅 Sat, 18 Jul 2026

### 4. [What does "playing politics" mean for software engineers?](https://seangoedecke.com/playing-politics/)
📍 seangoedecke.com | 📅 Tue, 14 Jul 2026

### 5. [Microsoft Patches a Record 570 Security Flaws](https://krebsonsecurity.com/2026/07/microsoft-patches-a-record-570-security-flaws/)
📍 krebsonsecurity.com | 📅 Tue, 14 Jul 2026

---
*报告由 Unified Intelligence Engine V2 自动生成*