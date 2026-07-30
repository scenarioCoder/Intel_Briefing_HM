# 每日商业情报简报: 2026-07-30


**日期:** 2026-07-30
**生成时间:** 01:03
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [AI's top startups are barely publishing their research](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research)
📍 Hacker News | 🔥 166 points | 🕒 3 hours ago

### 2. [The coolest use for the Vision Pro](https://christianselig.com/2026/07/vision-pro-house/)
📍 Hacker News | 🔥 360 points | 🕒 4 hours ago

### 3. [Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac](https://github.com/drumih/turbo-fieldfare)
📍 Hacker News | 🔥 635 points | 🕒 9 hours ago

### 4. [Superlogical](https://www.superlogical.com/)
📍 Hacker News | 🔥 511 points | 🕒 9 hours ago

### 5. [Keychron announces first open-source firmware for gaming mice](https://www.digitalfoundry.net/news/2026/07/keychron-announces-first-open-source-firmware-for-gaming-mice)
📍 Hacker News | 🔥 278 points | 🕒 8 hours ago

### 6. [The Cold Email](https://zachholman.com/posts/cold-email)
📍 Hacker News | 🔥 70 points | 🕒 3 hours ago

### 7. [Anatomy of a Frontier Lab Agent Intrusion: A Timeline of the July 2026 Incident](https://huggingface.co/blog/agent-intrusion-technical-timeline)
📍 Hacker News | 🔥 280 points | 🕒 6 hours ago

### 8. [Kimi K3-256k](https://www.kimi.com/code/docs/en/kimi-code/models)
📍 Hacker News | 🔥 331 points | 🕒 5 hours ago

### 9. [KOReader](https://koreader.rocks/)
📍 Hacker News | 🔥 657 points | 🕒 13 hours ago

### 10. [LLM Honeypot](https://llm2human.pages.dev/)
📍 Hacker News | 🔥 26 points | 🕒 2 hours ago

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [微软新增数据中心租约超1300亿美元](https://36kr.com/newsflashes/3917435911007621)
📍 36Kr | 🕒 1分钟前

### 2. [狂揽80亿美元估值，黑石推动三明治连锁店Jersey Mike's冲刺IPO](https://36kr.com/newsflashes/3917422152019587)
📍 36Kr | 🕒 4分钟前

### 3. [中信建投：看好重卡出口高景气及业绩强兑现](https://36kr.com/newsflashes/3917420858896003)
📍 36Kr | 🕒 7分钟前

### 4. [耐心资本密集落子，央企系基金加速布局硬科技](https://36kr.com/newsflashes/3917413432225160)
📍 36Kr | 🕒 9分钟前

### 5. [“翻倍基”数量锐减，绩优基金之间差距拉开](https://36kr.com/newsflashes/3917412792020359)
📍 36Kr | 🕒 12分钟前

### 6. [两市融资余额减少255.48亿元](https://36kr.com/newsflashes/3917422466035077)
📍 36Kr | 🕒 14分钟前

### 7. [强生下调全年调整后运营每股收益预期](https://36kr.com/newsflashes/3917411790515585)
📍 36Kr | 🕒 17分钟前

### 8. [摩根大通将美联储加息预期提前至12月](https://36kr.com/newsflashes/3917408113274241)
📍 36Kr | 🕒 19分钟前

### 9. [华泰证券：8月电池排产环比增长，看好本轮锂电涨价周期](https://36kr.com/newsflashes/3917404151426439)
📍 36Kr | 🕒 21分钟前

### 10. [中小银行理财业务迁徙：自营产品加速出清，代销成转型主航道](https://36kr.com/newsflashes/3917403746152072)
📍 36Kr | 🕒 23分钟前

## 📚 学术前沿 (Research)
> ArXiv AI/ML Papers

### 1. [Pass the Baton: Trajectory-Relayed On-Policy Distillation](https://arxiv.org/abs/2607.26057v1)
> ⚡ On-policy distillation (OPD) grounds token-level supervision in the student's ow...
👤 Haolei Xu, Xiaowen Xu | 📅 2026-07-28

**详情:** On-policy distillation (OPD) grounds token-level supervision in the student's own trajectory, yet suffers from prefix failure: once the student commits to a wrong reasoning direction, all subsequent generation builds on this deviation, producing misdirected continuations that elicit unreliable supervision and waste compute. We identify a teacher-student continuation asymmetry on failed prefixes, where the teacher tends to redirect while the student continues along the original direction, and convert it into a label-free handoff trigger in Relay On-Policy Distillation (Relay-OPD). During training, Relay-OPD constructs relay trajectories by letting the teacher briefly take over at detected trigger points to produce a teacher leg, after which the student resumes and is optimized on the resulting trajectory. A limited relay budget concentrates intervention on critical early positions while limiting departure from the student policy. With a Qwen3-4B-Instruct-2507 teacher and Qwen3-0.6B/1.7B-Non-Thinking students on eight mathematical reasoning benchmarks, Relay-OPD achieves the best or second-best results on every benchmark, outperforming standard OPD by +5.73% and the strongest baseline FastOPD by +1.49% on average for 1.7B, with consistent gains at 0.6B. Training trajectory length is reduced by over 50%.

### 2. [$π\mathbf{R}^2$: Reactive Real-time Flow Policies](https://arxiv.org/abs/2607.26055v1)
> ⚡ Generalist manipulation policies increasingly take the form of action-chunking f...
👤 Sungjae Park, Shubham Tulsiani | 📅 2026-07-28

**详情:** Generalist manipulation policies increasingly take the form of action-chunking flow policies built on large pretrained backbones. Such chunks run open-loop, so the policy cannot react to sensory input arriving mid-execution, sacrificing \emph{reactivity}. Replanning more often would restore it, but the perception-to-action pipeline (a large backbone plus multiple denoising steps) is too slow: this \emph{latency} forbids frequent replanning and leaves committed actions stale, making such policies ill-suited for dynamic, closed-loop control. We present $π\mathbf{R}^2$, which makes these policies reactive and real-time while retaining large backbones, expressive multi-modal policies, and multi-action prediction. Built on the per-position noise schedule of diffusion forcing, $π\mathbf{R}^2$ contributes two ideas. First, it splits conditioning into a fast channel (proprioception, fresh every tick) and an asynchronously updated slow channel (vision-language features), so the policy reacts to proprioception within a chunk while tolerating stale vision. Second, a latency-adaptive flow schedule treats in-flight actions as inpainting conditioning and emits actions in one denoising step per call, letting one trained model adapt to varying hardware latency. Requiring minimal modification to existing architectures, $π\mathbf{R}^2$ can be finetuned from a pretrained policy: applied to GR00T-N1.7 on a real xArm6+XHand platform, it replans closed-loop roughly $4\times$ faster than the base policy (~$25$Hz on an A5000 GPU), acting on a fresh observation every $40$ms. Across simulation and real-world manipulation tasks, $π\mathbf{R}^2$ improves the success rate by up to $23\%$ in simulation and $30\%$ in the real world over the strongest baseline. Project page: https://pi-r2-flow.github.io/

### 3. [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](https://arxiv.org/abs/2607.26041v1)
> ⚡ Computer-use agents (CUAs) increasingly act through desktop GUIs to complete lon...
👤 Abhishek Pillai, Samir Kumar Nayak | 📅 2026-07-28

**详情:** Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates whether a model can reconstruct the causal, task-relevant transition produced by an action- crucial for rejecting stale observations, verifying progress, and recovering from failure. This is difficult because inference, remote input, app rendering, and screenshot capture are asynchronous: the next observation may be delayed, occluded, transient, or unrelated, then misread as progress and carried into subsequent planning. We introduce Desktop-Delta Bench (DDB), an offline step-level benchmark with 2,013 human-verified instances from novel, multi-app Linux trajectories across ~15 applications and 50 task domains. DDB trajectories targets 3 failure dimensions- state verification, source tracking, and context-aware control- through 2 complementary tasks: 463 3-frame temporal-ordering instances, including 105 with a cross-trajectory decoy, and 1,550 before-after pairs labeled from 5 actions + its payload. We evaluate 8 closed and open-source model families across 32 ordering and 16 single-action settings, observing consistent gaps. Ordering remains unsaturated: best non-decoy and decoy exact-match rates are 65.1% and 65.7%. Task context improves decoy identification by 6.9 percentage points but reduces non-decoy exact match by 2.2 points; error analysis reveals systematic copying of the presented A-B-C order. Single-action results show that inferring the action family is harder than locating it: click F1 is 0.96 vs, 0.76 for drag, while recognized drags are generally localized well. DDB, thus, complements end-to-end benchmarks by filling the missing diagnostic layer between GUI grounding and final task success, enabling targeted improvements to desktop CUA verification, reliability, and recovery.

### 4. [Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment](https://arxiv.org/abs/2607.26034v1)
> ⚡ Technological races create tension between speed and safety: actors may gain by ...
👤 Elias Fernández Domingos, The Anh Han | 📅 2026-07-28

**详情:** Technological races create tension between speed and safety: actors may gain by moving faster than competitors, even when risky development is harmful. This is prominent in debates about artificial intelligence (AI), where competitive pressure is often argued to incentivise riskier, less safety-conscious development. We study this using a framed behavioural experiment based on an idealised AI race, in which paired participants repeatedly chose between Safe and Unsafe development under an uncertain time horizon. Unsafe development gave faster progress and higher immediate payoffs but accumulated private risk up to a treatment-specific maximum of 10\%, 60\%, or 90\%; the race's competitive structure was held constant, and only this maximum risk varied. Neither the pre-registered comparison between risk levels nor the role of elicited risk preferences was supported by the data. Instead, exploratory analyses motivated by the task's repeated structure show that Unsafe behaviour is shaped less by risk preferences than by the evolving strategic state of the race: participants are more likely to choose Unsafe after their opponent does so, being ahead reduces Unsafe play while falling behind increases it, and first-round choices predict later behaviour. To interpret these effects we introduce a reduced evolutionary model with four strategies -- Always Safe, Always Unsafe, Conditionally Safe, and Conditionally Antisocial Safe -- which reproduces the treatment effect and shows how conditional Unsafe behaviour can be favoured by competitive race dynamics. Together, the experiment and model show that unsafe development can emerge from early behavioural momentum, opponent behaviour, and fear of falling behind, rather than from risk preferences alone, suggesting policy should focus on reducing competitive pressure and promoting cooperation in AI development rather than only individual risk.

### 5. [CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer](https://arxiv.org/abs/2607.26023v1)
> ⚡ Graph foundation models (GFMs) have emerged as a promising paradigm for transfer...
👤 Ankang Yang, Jitao Zhao | 📅 2026-07-28

**详情:** Graph foundation models (GFMs) have emerged as a promising paradigm for transferring knowledge across graph domains and tasks. Real-world graphs associate nodes with text, images, and other modalities, making multimodal graphs essential for representing complex entities and relations. Moreover, collecting labels and adapting models for every new graph domain is costly and often infeasible, motivating zero-shot transfer. Unfortunately, zero-shot transfer on multimodal graphs remains underexplored. Existing GNN-based graph foundation models typically require downstream adaptation, whereas LLM-based graph methods mainly address unimodal graphs or tasks within a single domain. This setting presents two key challenges. First, models must generalize knowledge from individual modalities while capturing transferable cross-modal relations. Second, without target-domain fine-tuning, node representations remain entangled with domain-specific structures and modality-specific characteristics, obscuring shared concepts in unseen domains. To address these challenges, we propose CHARM, a multimodal graph foundation model with hierarchical context modeling for zero-shot transfer. CHARM replaces isolated raw nodes with hierarchical graph contexts that capture multimodal semantics and cross-modal relations. These contexts map domain-specific node patterns to shared high-level concepts, reducing reliance on target-domain supervision or adaptation. A modality-aware graph context encoder integrates multimodal information with graph structure and converts the resulting representations into graph tokens for a large language model . Experiments show consistent improvements on zero-shot multimodal graph tasks.

## 💎 产品精选 (Product Gems)
> Product Hunt Today

### 1. [Acti](https://www.producthunt.com/posts/acti-3)
> Agentic keyboard for mobile commands and search
🔥 915 votes

### 2. [OpenSEO](https://www.producthunt.com/posts/openseo)
> The open source Ahrefs alternative
🔥 907 votes

### 3. [Pazi](https://www.producthunt.com/posts/pazi-2)
> Vibe code business operations
🔥 893 votes

### 4. [Context.dev](https://www.producthunt.com/posts/context-dev-2)
> One API to scrape, enrich, and extract the internet
🔥 877 votes

### 5. [AnySearch](https://www.producthunt.com/posts/anysearch-3)
> Real-time structured search trusted by agents and developers
🔥 769 votes

### 6. [Fuzzy AI](https://www.producthunt.com/posts/fuzzy-ai-2)
> We warm your prospects before reaching out
🔥 687 votes

### 7. [Glaze by Raycast](https://www.producthunt.com/posts/glaze-by-raycast-2)
> Create your own Mac apps by chatting with AI
🔥 681 votes

### 8. [Sim](https://www.producthunt.com/posts/sim-3)
> Open-source workspace for AI agents and workflows
🔥 672 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [兄弟们都买了什么新能源车？理想 I6、ModelY、极氪？](https://www.v2ex.com/t/1230594)
💬 171 replies

### 2. [你是在什么时候意识到自己已经不再年轻了？](https://www.v2ex.com/t/1230609)
💬 138 replies

### 3. [model Y 到底有啥魔力，体验了下感觉就是很普通一辆车，为啥卖这么好？](https://www.v2ex.com/t/1230740)
💬 129 replies

### 4. [好奇问下，你们碰到的第一台电脑是啥？](https://www.v2ex.com/t/1230623)
💬 114 replies

### 5. [观“存了 100w+ 太想躺平了”有感](https://www.v2ex.com/t/1230580)
💬 83 replies

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

### 1. [Adding a backup Internet WAN on my OPNsense Router](https://www.jeffgeerling.com/blog/2026/opnsense-backup-internet-gateway/)
📍 jeffgeerling.com | 📅 Thu, 23 Jul 2026

### 2. [Open Sauce and GPS time were my summer AI Antiseptics](https://www.jeffgeerling.com/blog/2026/open-sauce-gps-time-badge/)
📍 jeffgeerling.com | 📅 Wed, 22 Jul 2026

### 3. [You don't have to be smart if you can think clearly](https://seangoedecke.com/you-dont-have-to-be-smart-if-you-think-clearly/)
📍 seangoedecke.com | 📅 Wed, 29 Jul 2026

### 4. [LLMs reward expertise](https://seangoedecke.com/llms-reward-expertise/)
📍 seangoedecke.com | 📅 Fri, 24 Jul 2026

### 5. [LG to Ban Residential Proxies from Smart TV Apps](https://krebsonsecurity.com/2026/07/lg-to-ban-residential-proxies-from-smart-tv-apps/)
📍 krebsonsecurity.com | 📅 Wed, 22 Jul 2026

---
*报告由 Unified Intelligence Engine V2 自动生成*