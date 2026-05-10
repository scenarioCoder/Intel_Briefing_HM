# 每日商业情报简报: 2026-05-10


**日期:** 2026-05-10
**生成时间:** 01:26
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [Bun's experimental Rust rewrite hits 99.8% test compatibility on Linux x64 glibc](https://twitter.com/jarredsumner/status/2053047748191232310)
📍 Hacker News | 🔥 403 points | 🕒 6 hours ago

### 2. [Internet Archive Switzerland](https://blog.archive.org/2026/05/06/internet-archive-switzerland-expanding-a-global-mission-to-preserve-knowledge/)
📍 Hacker News | 🔥 531 points | 🕒 13 hours ago

### 3. [Rust but Lisp](https://github.com/ThatXliner/rust-but-lisp)
📍 Hacker News | 🔥 65 points | 🕒 3 hours ago

### 4. [The Serial TTL connector we deserve](https://kohlschuetter.github.io/blog/posts/2026/05/07/serial-ttl-connector/)
📍 Hacker News | 🔥 38 points | 🕒 3 hours ago

### 5. [I’ve banned query strings](https://chrismorgan.info/no-query-strings)
📍 Hacker News | 🔥 257 points | 🕒 8 hours ago

### 6. [Local privilege escalation via execve()](https://www.freebsd.org/security/advisories/FreeBSD-SA-26:13.exec.asc)
📍 Hacker News | 🔥 82 points | 🕒 4 hours ago

### 7. [Show HN: I made a Clojure-like language in Go, boots in 7ms](https://github.com/nooga/let-go)
📍 Hacker News | 🔥 85 points | 🕒 4 hours ago

### 8. [Zed Editor Theme-Builder](https://zed.dev/theme-builder)
📍 Hacker News | 🔥 155 points | 🕒 7 hours ago

### 9. [Making your own programming language is easier than you think (but also harder)](https://lisyarus.github.io/blog/posts/making-your-own-programming-language.html)
📍 Hacker News | 🔥 41 points | 🕒 4 hours ago

### 10. [CPanel's Black Week: 3 New Vulnerabilities Patched After Attack on 44k Servers](https://www.copahost.com/blog/cpanels-black-week-three-new-vulnerabilities-patched-after-ransomware-attack-on-44000-servers/)
📍 Hacker News | 🔥 107 points | 🕒 8 hours ago

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [下周重磅日程：全球聚焦中美](https://wallstreetcn.com/charts/41959043)
📍 WallStreetCN | 🕒 01:22

### 2. [不要浪费一场好危机：VLCC升格“战略资产”，原油补库需求“虽迟但到”](https://wallstreetcn.com/member/articles/3771820)
📍 WallStreetCN | 🕒 01:07

### 3. [丰田陷入“增收不增利”漩涡](https://wallstreetcn.com/articles/3771911)
📍 WallStreetCN | 🕒 01:06

### 4. [当OpenAI和Anthropic下场“抢生意”，Palantir的真对手来了](https://wallstreetcn.com/articles/3771914)
📍 WallStreetCN | 🕒 01:04

### 5. [牵动全球市场的关键问题：伊朗危机走向何方？](https://wallstreetcn.com/themes/1008388)
📍 WallStreetCN | 🕒 

### 6. [云大厂：资本开支 vs 股票回购](https://wallstreetcn.com/charts/41959042)
📍 WallStreetCN | 🕒 00:18

### 7. [2026的芯片股 vs 1999的纳指](https://wallstreetcn.com/charts/41959041)
📍 WallStreetCN | 🕒 00:08

### 8. [“已锁定美国目标”，伊朗革命卫队警告：侵犯伊朗船只将引发猛烈打击](https://wallstreetcn.com/livenews/3101094)
📍 WallStreetCN | 🕒 22:04

### 9. [涨太多的苦恼：美国投资者激辩“当下是1999年再现吗？”](https://wallstreetcn.com/charts/41959040)
📍 WallStreetCN | 🕒 14:11

### 10. [中国汽车工业协会：网传“新能源车企因锁电问题被约谈、立案”为不实信息](https://wallstreetcn.com/livenews/3101076)
📍 WallStreetCN | 🕒 13:00

## 📚 学术前沿 (Research)
> ArXiv AI/ML Papers

### 1. [ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation](https://arxiv.org/abs/2605.06667v1)
> ⚡ For artistic applications, video generation requires fine-grained control over b...
👤 Omar El Khalifi, Thomas Rossi | 📅 2026-05-07

**详情:** For artistic applications, video generation requires fine-grained control over both performance and cinematography, i.e., the actor's motion and the camera trajectory. We present ActCam, a zero-shot method for video generation that jointly transfers character motion from a driving video into a new scene and enables per-frame control of intrinsic and extrinsic camera parameters. ActCam builds on any pretrained image-to-video diffusion model that accepts conditioning in terms of scene depth and character pose. Given a source video with a moving character and a target camera motion, ActCam generates pose and depth conditions that remain geometrically consistent across frames. We then run a single sampling process with a two-phase conditioning schedule: early denoising steps condition on both pose and sparse depth to enforce scene structure, after which depth is dropped and pose-only guidance refines high-frequency details without over-constraining the generation. We evaluate ActCam on multiple benchmarks spanning diverse character motions and challenging viewpoint changes. We find that, compared to pose-only control and other pose and camera methods, ActCam improves camera adherence and motion fidelity, and is preferred in human evaluations, especially under large viewpoint changes. Our results highlight that careful camera-consistent conditioning and staged guidance can enable strong joint camera and motion control without training. Project page: https://elkhomar.github.io/actcam/.

### 2. [UniPool: A Globally Shared Expert Pool for Mixture-of-Experts](https://arxiv.org/abs/2605.06665v1)
> ⚡ Modern Mixture-of-Experts (MoE) architectures allocate expert capacity through a...
👤 Minbin Huang, Han Shi | 📅 2026-05-07

**详情:** Modern Mixture-of-Experts (MoE) architectures allocate expert capacity through a rigid per-layer rule: each transformer layer owns a separate expert set. This convention couples depth scaling with linear expert-parameter growth and assumes that every layer needs isolated expert capacity. However, recent analyses and our routing probe challenge this allocation rule: replacing a deeper layer's learned top-k router with uniform random routing drops downstream accuracy by only 1.0-1.6 points across multiple production MoE models. Motivated by this redundancy, we propose UniPool, an MoE architecture that treats expert capacity as a global architectural budget by replacing per-layer expert ownership with a single shared pool accessed by independent per-layer routers. To enable stable and balanced training under sharing, we introduce a pool-level auxiliary loss that balances expert utilization across the entire pool, and adopt NormRouter to provide sparse and scale-stable routing into the shared expert pool. Across five LLaMA-architecture model scales (182M, 469M, 650M, 830M, and 978M parameters) trained on 30B tokens from the Pile, UniPool consistently improves validation loss and perplexity over the matched vanilla MoE baselines. Across these scales, UniPool reduces validation loss by up to 0.0386 relative to vanilla MoE. Beyond raw loss improvement, our results identify pool size as an explicit depth-scaling hyperparameter: reduced-pool UniPool variants using only 41.6%-66.7% of the vanilla expert-parameter budget match or outperform layer-wise MoE at the tested scales. This shows that, under a shared-pool design, expert parameters need not grow linearly with depth; they can grow sublinearly while remaining more efficient and effective than vanilla MoE. Further analysis shows that UniPool's benefits compose with finer-grained expert decomposition.

### 3. [BAMI: Training-Free Bias Mitigation in GUI Grounding](https://arxiv.org/abs/2605.06664v1)
> ⚡ GUI grounding is a critical capability for enabling GUI agents to execute tasks ...
👤 Borui Zhang, Bo Zhang | 📅 2026-05-07

**详情:** GUI grounding is a critical capability for enabling GUI agents to execute tasks such as clicking and dragging. However, in complex scenarios like the ScreenSpot-Pro benchmark, existing models often suffer from suboptimal performance. Utilizing the proposed \textbf{Masked Prediction Distribution (MPD)} attribution method, we identify that the primary sources of errors are twofold: high image resolution (leading to precision bias) and intricate interface elements (resulting in ambiguity bias). To address these challenges, we introduce \textbf{Bias-Aware Manipulation Inference (BAMI)}, which incorporates two key manipulations, coarse-to-fine focus and candidate selection, to effectively mitigate these biases. Our extensive experimental results demonstrate that BAMI significantly enhances the accuracy of various GUI grounding models in a training-free setting. For instance, applying our method to the TianXi-Action-7B model boosts its accuracy on the ScreenSpot-Pro benchmark from 51.9\% to 57.8\%. Furthermore, ablation studies confirm the robustness of the BAMI approach across diverse parameter configurations, highlighting its stability and effectiveness. Code is available at https://github.com/Neur-IO/BAMI.

### 4. [Verifier-Backed Hard Problem Generation for Mathematical Reasoning](https://arxiv.org/abs/2605.06660v1)
> ⚡ Large Language Models (LLMs) demonstrate strong capabilities for solving scienti...
👤 Yuhang Lai, Jiazhan Feng | 📅 2026-05-07

**详情:** Large Language Models (LLMs) demonstrate strong capabilities for solving scientific and mathematical problems, yet they struggle to produce valid, challenging, and novel problems - an essential component for advancing LLM training and enabling autonomous scientific research. Existing problem generation approaches either depend on expensive human expert involvement or adopt naive self-play paradigms, which frequently yield invalid problems due to reward hacking. This work introduces VHG, a verifier-enhanced hard problem generation framework built upon three-party self-play. By integrating an independent verifier into the conventional setter-solver duality, our design constrains the setter's reward to be jointly determined by problem validity (evaluated by the verifier) and difficulty (assessed by the solver). We instantiate two verifier variants: a Hard symbolic verifier and a Soft LLM-based verifier, with evaluations conducted on indefinite integral tasks and general mathematical reasoning tasks. Experimental results show that VHG substantially outperforms all baseline methods by a clear margin.

### 5. [Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less](https://arxiv.org/abs/2605.06654v1)
> ⚡ Optimizers play an important role in both pretraining and finetuning stages when...
👤 Yuxing Liu, Jianyu Wang | 📅 2026-05-07

**详情:** Optimizers play an important role in both pretraining and finetuning stages when training large language models (LLMs). In this paper, we present an observation that full finetuning with the same optimizer as in pretraining achieves a better learning-forgetting tradeoff, i.e., forgetting less while achieving the same or better performance on the new task, than other optimizers and, possibly surprisingly, LoRA, during the supervised finetuning (SFT) stage. We term this phenomenon optimizer-model consistency. To better understand it, through controlled experiments and theoretical analysis, we show that: 1) optimizers can shape the models by having regularization effects on the activations, leading to different landscapes around the pretrained checkpoints; 2) in response to this regularization effect, the weight update in SFT should follow some specific structures to lower forgetting of the knowledge learned in pretraining, which can be obtained by using the same optimizer. Moreover, we specifically compare Muon and AdamW when they are employed throughout the pretraining and SFT stages and find that Muon performs worse when finetuned for reasoning tasks. With a synthetic language modeling experiment, we demonstrate that this can come from Muon's strong tendency towards rote memorization, which may hurt pattern acquisition with a small amount of data, as for SFT.

## 💎 产品精选 (Product Gems)
> Product Hunt Today

### 1. [Fathom 3.0](https://www.producthunt.com/posts/fathom-3-0)
> AI meeting notes: now bot-free, in ChatGPT & Claude + more
🔥 773 votes

### 2. [Plurai](https://www.producthunt.com/posts/plurai)
> Vibe-train evals and guardrails tailored to your use case
🔥 741 votes

### 3. [Clera](https://www.producthunt.com/posts/clera)
> An AI agent matching candidates to the right roles.
🔥 712 votes

### 4. [Dune](https://www.producthunt.com/posts/dune-5)
> Context-aware Mac keypad to automate workflows + meetings
🔥 632 votes

### 5. [Kilo Code v7 for VS Code](https://www.producthunt.com/posts/kilo-code-v7-for-vs-code)
> Parallel agents, diff reviewer, and multi-model comparisons
🔥 629 votes

### 6. [Open Wearables](https://www.producthunt.com/posts/open-wearables-3)
> Open infrastructure for wearable-powered health products.
🔥 625 votes

### 7. [RankAI](https://www.producthunt.com/posts/rankai-2)
> RankAI autonomously gets you buyers from Google & AI Search
🔥 605 votes

### 8. [Claude Code Routines](https://www.producthunt.com/posts/claude-code-routines)
> Put Claude Code tasks on autopilot with smart routines
🔥 589 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [兄弟们你们加薪最低的比例是多少，有没有像我一样的小丑](https://www.v2ex.com/t/1211380)
💬 115 replies

### 2. [26 岁， 3 次考公失败、0 工作经验，现在年轻人的处境确实不容易](https://www.v2ex.com/t/1211458)
💬 114 replies

### 3. [无法接受自己的错误](https://www.v2ex.com/t/1211383)
💬 96 replies

### 4. [五一期间认识的一个初中老师退休工资一个月 9000+，想去当老师了](https://www.v2ex.com/t/1211440)
💬 85 replies

### 5. [老哥们同意这段话吗?在一个家族中第一个接触金融、股票、基金、债券、期货的人，看似是不务正业，实则是为整个家族完成了一场认知的提升](https://www.v2ex.com/t/1211422)
💬 78 replies

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

### 1. [HomePod mini feels like magic, but it's just good timing](https://www.jeffgeerling.com/blog/2026/homepod-mini-feels-like-magic--but-it-s-just-good-timing/)
📍 jeffgeerling.com | 📅 Fri, 08 May 2026

### 2. [SBC Clusters are a terrible value, but they're fun anyway](https://www.jeffgeerling.com/blog/2026/deskpi-super4c-sbc-cluster/)
📍 jeffgeerling.com | 📅 Fri, 01 May 2026

### 3. [AI makes weak engineers less harmful](https://seangoedecke.com/ai-makes-weak-engineers-less-harmful/)
📍 seangoedecke.com | 📅 Sat, 09 May 2026

### 4. [Notes on incidents](https://seangoedecke.com/notes-on-incidents/)
📍 seangoedecke.com | 📅 Fri, 08 May 2026

### 5. [Canvas Breach Disrupts Schools & Colleges Nationwide](https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/)
📍 krebsonsecurity.com | 📅 Fri, 08 May 2026

---
*报告由 Unified Intelligence Engine V2 自动生成*