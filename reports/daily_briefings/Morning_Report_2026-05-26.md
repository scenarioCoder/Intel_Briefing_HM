# 每日商业情报简报: 2026-05-26


**日期:** 2026-05-26
**生成时间:** 01:31
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [Using AI to write better code more slowly](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/)
📍 Hacker News | 🔥 113 points | 🕒 2 hours ago

### 2. [Norway's 2 petabytes of Huawei flash storage and LLM training](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910)
📍 Hacker News | 🔥 154 points | 🕒 5 hours ago

### 3. [Taking a walk may lead to more creativity than sitting, study finds (2014)](https://www.apa.org/news/press/releases/2014/04/creativity-walk)
📍 Hacker News | 🔥 44 points | 🕒 2 hours ago

### 4. [Exit IP VPN servers mitigation rollout](https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout)
📍 Hacker News | 🔥 261 points | 🕒 7 hours ago

### 5. [California moves to exempt Linux from its age-verification law after backlash](https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law)
📍 Hacker News | 🔥 633 points | 🕒 7 hours ago

### 6. [How Shamir's Secret Sharing Works](https://ente.com/blog/how-shamirs-secret-sharing-works/)
📍 Hacker News | 🔥 25 points | 🕒 2 hours ago

### 7. [Show HN: Write your BPF programs in Go, not C](https://github.com/boratanrikulu/gobee)
📍 Hacker News | 🔥 57 points | 🕒 5 hours ago

### 8. [Hacker News front page as a site](https://thefrontpage.dev/)
📍 Hacker News | 🔥 107 points | 🕒 5 hours ago

### 9. [CVE-2026-28952: Apple macOS 26.5 Kernel Vuln found by Claude](https://support.apple.com/en-us/127115)
📍 Hacker News | 🔥 58 points | 🕒 1 hour ago

### 10. [Magnifica Humanitas](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html)
📍 Hacker News | 🔥 1328 points | 🕒 15 hours ago

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [A股集体低开，宇树机器人概念走强，恒生科技指数涨1.9%，华虹、中芯国际大涨15%](https://wallstreetcn.com/articles/3773113)
📍 WallStreetCN | 🕒 01:27

### 2. [黄仁勋：奋斗是因为“早年艰辛”，希望死在工作岗位上](https://wallstreetcn.com/charts/41959125)
📍 WallStreetCN | 🕒 01:25

### 3. [决定AI牛市的关键变量是什么？](https://wallstreetcn.com/articles/3773111)
📍 WallStreetCN | 🕒 01:24

### 4. [线控底盘：解锁高阶智驾的“最后拼图”，2026年产业化元年已至](https://wallstreetcn.com/member/articles/3772896)
📍 WallStreetCN | 🕒 01:19

### 5. [“AI狂潮”不在乎成本高低--这是当前全球宏观最大的影响因子](https://wallstreetcn.com/articles/3773109)
📍 WallStreetCN | 🕒 01:16

### 6. [贝莱德基金经理：美联储降息理由"已然充分"](https://wallstreetcn.com/articles/3773110)
📍 WallStreetCN | 🕒 01:13

### 7. [ComputeX 2026即将开幕，黄仁勋、苏姿丰和陈立武先后抵台“密访”供应链](https://wallstreetcn.com/articles/3773106)
📍 WallStreetCN | 🕒 00:43

### 8. [华为提出“韬定律”，关注半导体工艺发展新方向](https://wallstreetcn.com/articles/3773108)
📍 WallStreetCN | 🕒 00:35

### 9. [AI最大的“敌人” 是人类的欲望](https://wallstreetcn.com/member/articles/3773098)
📍 WallStreetCN | 🕒 00:18

### 10. [美伊协议尚在“拉锯”，以色列下令“猛踩油门”打击黎真主党](https://wallstreetcn.com/articles/3773107)
📍 WallStreetCN | 🕒 00:17

## 📚 学术前沿 (Research)
> ArXiv AI/ML Papers

### 1. [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904v1)
> ⚡ Agent skills today are hand-crafted, generated one-shot, or evolved through loos...
👤 Yifan Yang, Ziyang Gong | 📅 2026-05-22

**详情:** Agent skills today are hand-crafted, generated one-shot, or evolved through loosely controlled self-revision, none of which behaves like a deep-learning optimizer for the skill, and none of which reliably improves over its starting point under feedback. We argue the skill should instead be trained as the external state of a frozen agent, with the same discipline that makes weight-space optimization reproducible. SkillOpt is, to our knowledge, the first systematic controllable text-space optimizer for agent skills: a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document, and an edit is accepted only when it strictly improves a held-out validation score. A textual learning-rate budget, rejected-edit buffer, and epoch-wise slow/meta update make skill training stable while adding zero inference-time model calls at deployment. Across six benchmarks, seven target models, and three execution harnesses (direct chat, Codex, Claude Code), SkillOpt is best or tied on all 52 evaluated (model, benchmark, harness) cells and beats every per-cell competitor among human, one-shot LLM, Trace2Skill, TextGrad, GEPA, and EvoSkill skills. On GPT-5.5 it lifts the average no-skill accuracy by +23.5 points in direct chat, by +24.8 inside the Codex agentic loop, and by +19.1 inside Claude Code. Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization.

### 2. [LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws](https://arxiv.org/abs/2605.23901v1)
> ⚡ Existing scaling laws for Large Language Models (LLMs), predominantly monotonic ...
👤 Xu Ouyang, Deyi Liu | 📅 2026-05-22

**详情:** Existing scaling laws for Large Language Models (LLMs), predominantly monotonic power laws, fail to explain emerging non-monotonic phenomena such as catastrophic overtraining and quantization-induced degradation, where performance deteriorates despite increased compute. We propose the Shannon Scaling Law, a unified theoretical framework that models LLM training as information transmission over a noisy channel, grounded in the Shannon-Hartley theorem. By mapping model parameters to channel bandwidth and training tokens to signal power, our formulation explicitly captures the interaction between learning signal and intrinsic noise. This perspective reveals a fundamental Shannon capacity for LLMs: scaling model size or data without preserving a sufficient signal-to-noise ratio (SNR) inevitably amplifies noise, inducing a transition from monotonic improvement to U-shaped performance degradation. We validate our theory through experiments on Pythia and OLMo2 under perturbations, including Gaussian noise, quantization and supervised fine-tuning on math, QA and code tasks. The Shannon Scaling Law consistently outperforms classical scaling laws and recent perturbation-aware laws, achieving strong $R^2$ scores and accurately capturing loss basins missed by prior approaches. It also extrapolates: fitted on $\leq$6.9B Pythia models with $\leq$180B tokens, it predicts the unseen 12B model up to 307B tokens at pooled $R^2{=}0.847$, while monotonic baselines collapse.

### 3. [From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills](https://arxiv.org/abs/2605.23899v1)
> ⚡ Language agents increasingly improve by reusing \emph{skills} -- structured proc...
👤 Zisu Huang, Jingwen Xu | 📅 2026-05-22

**详情:** Language agents increasingly improve by reusing \emph{skills} -- structured procedural artifacts distilled from past experience. In particular, \emph{domain-level} and \emph{model-generated} skills are especially promising. They offer fast adaptation within a domain by encoding domain-specific recurring procedures, and they scale beyond labor-intensive hand-crafting. However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail. To close this gap, we build a utility-grounded evaluation framework that provides systematic experimental results across extractors and target agents, covering five diverse agentic task domains. We find that model-generated skills are beneficial on average but exhibit non-trivial negative transfer, and that neither extractors nor targets behave uniformly. A model can be a strong extractor yet a weak consumer, or vice versa, with skill utility independent of model scale or baseline task strength. To explain these patterns, we then dissect each lifecycle stage in depth, analyzing how experience composition shapes skill quality, what properties characterize useful skills, and how the same skill transfers across different consumers. Finally, we translate these findings into a concrete \emph{meta-skill} that guides skill extraction toward the features tied to actual utility, which consistently improves skill quality across domains and substantially reduces negative transfer.

### 4. [SPACENUM: Revisiting Spatial Numerical Understanding in VLMs](https://arxiv.org/abs/2605.23898v1)
> ⚡ Vision-Language Models (VLMs) are increasingly deployed in embodied environments...
👤 Jianshu Zhang, Yijiang Li | 📅 2026-05-22

**详情:** Vision-Language Models (VLMs) are increasingly deployed in embodied environments, where they need produce numerical outputs such as action magnitudes and spatial coordinates. Although these numbers appear meaningful, it remains unclear whether these numerical outputs are genuinely grounded in spatial perception. Therefore, in this work, we revisit spatial numerical understanding through SpaceNum, a unified framework that captures two complementary settings: numbers as dynamic transitions during spatial exploration, and numbers as static layouts in spatial reasoning. We formulate two bidirectional tasks, Num2Space and Space2Num, to evaluate how well VLMs map between vision-side spatial structure and language-side numerical representations. We systematically study whether current VLMs truly understand numerical values in spatial settings. Across dynamic transitions and static layouts, we find that models largely fail to ground numbers in spatial meaning and often perform close to random guess. Through error analysis, reasoning trace analysis, and controlled interventions, we show that current VLMs rely heavily on shallow spatial cues, struggle to build stable coordinate-aware representations, and fail to abstract structured spatial layouts from visual observations. We further show that explicit reasoning provides only marginal gains, while tuning can partially improve spatial numerical understanding and transfer to external spatial reasoning benchmarks.

### 5. [ETCHR: Editing To Clarify and Harness Reasoning](https://arxiv.org/abs/2605.23897v1)
> ⚡ Multimodal Large Language Models have advanced visual reasoning, yet a purely te...
👤 Beichen Zhang, Yuhong Liu | 📅 2026-05-22

**详情:** Multimodal Large Language Models have advanced visual reasoning, yet a purely textual chain of thought remains a bottleneck for questions that require fine-grained focus or view transformations. The ''think with images'' paradigm narrows this gap, but existing approaches are either constrained by fixed predefined toolkits or produce noisy intermediate images from unified multimodal methods. We pursue a third option: using a dedicated image editing model and decouple it with an understanding model. However, off-the-shelf image editors fail as reasoning assistants with two complementary gaps: a language-side gap, where editors trained as passive instruction-followers cannot map an abstract question to an appropriate visual transformation, and a generation-side gap, where edit correctness degrades as reasoning depth grows. Guided by this analysis, we introduce ETCHR (Editing To Clarify and Harness Reasoning), a question-conditioned, reasoning-aware image editor decoupled from the downstream understanding model and trained with a two-stage recipe targeted at the two gaps: Reasoning Imitation via supervised fine-tuning on edit trajectories, followed by Reasoning Enhancement with VLM-derived rewards for edit correctness and downstream reasoning accuracy. Since the editor is decoupled, ETCHR plugs into different open- and closed-source MLLMs in a training-free manner. Across five task families (fine-grained perception, chart understanding, logic reasoning, jigsaw restoration, and 3D understanding), ETCHR raises average Pass@1 from 55.95 to 60.77 (+4.82) with Qwen3-VL-8B, from 65.08 to 70.55 (+5.47) with Gemini-3.1-Flash-Lite, and from 76.55 to 81.16 (+4.61) with the 1T-parameter MoE model Kimi K2.5.

## 💎 产品精选 (Product Gems)
> Product Hunt Today

### 1. [Kilo Code v7 for VS Code](https://www.producthunt.com/posts/kilo-code-v7-for-vs-code)
> Parallel agents, diff reviewer, and multi-model comparisons
🔥 807 votes

### 2. [StoreClaw](https://www.producthunt.com/posts/storeclaw)
> Grow your store profits with agents that know how to sell
🔥 793 votes

### 3. [PollyReach](https://www.producthunt.com/posts/pollyreach)
> Give your agent a real number and voice to make calls.
🔥 783 votes

### 4. [Plurai](https://www.producthunt.com/posts/plurai)
> Vibe-train evals and guardrails tailored to your use case
🔥 780 votes

### 5. [Clera](https://www.producthunt.com/posts/clera)
> An AI agent matching candidates to the right roles.
🔥 733 votes

### 6. [RankSpot](https://www.producthunt.com/posts/rankspot)
> AI SEO Blog driven by deep competitor intelligence
🔥 659 votes

### 7. [Open Wearables](https://www.producthunt.com/posts/open-wearables-3)
> Open infrastructure for wearable-powered health products.
🔥 646 votes

### 8. [OpenHuman](https://www.producthunt.com/posts/openhuman)
> An open source AI harness built with the human in mind
🔥 646 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [彩礼是男方出还是男方父母出?](https://www.v2ex.com/t/1215213)
💬 227 replies

### 2. [有哪些东西，是你装修后最庆幸买的？](https://www.v2ex.com/t/1215221)
💬 162 replies

### 3. [花费近万元，跑了 8500km，我租车一年后的真实感受](https://www.v2ex.com/t/1215190)
💬 116 replies

### 4. [HyperAPI 的新老用户来领福利了，留 ID 加额度](https://www.v2ex.com/t/1215373)
💬 93 replies

### 5. [公司给每个研发分配了不限量 CC sonnet 4.6，每周发布额度消耗排行榜，如何能排名靠前些呢？](https://www.v2ex.com/t/1215243)
💬 91 replies

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

### 1. [News about Raspberry Pi 6 and Microcontroller Development](https://www.jeffgeerling.com/blog/2026/news-about-raspberry-pi-6-and-microcontroller-development/)
📍 jeffgeerling.com | 📅 Fri, 22 May 2026

### 2. [Wi-Wi Is Wireless Time Sync at 1 nanosecond](https://www.jeffgeerling.com/blog/2026/wi-wi-is-wireless-time-sync-less-than-5ns/)
📍 jeffgeerling.com | 📅 Tue, 19 May 2026

### 3. [The famous o3 "GeoGuessr" prompt did not work](https://seangoedecke.com/the-o3-geoguessr-prompt-did-not-work/)
📍 seangoedecke.com | 📅 Thu, 21 May 2026

### 4. [Prompts are technical debt too](https://seangoedecke.com/prompts-are-technical-debt-too/)
📍 seangoedecke.com | 📅 Wed, 20 May 2026

### 5. [Netherlands Seizes 800 Servers, Arrests 2 for Aiding Cyberattacks](https://krebsonsecurity.com/2026/05/netherlands-seizes-800-servers-arrests-2-for-aiding-cyberattacks/)
📍 krebsonsecurity.com | 📅 Mon, 25 May 2026

---
*报告由 Unified Intelligence Engine V2 自动生成*