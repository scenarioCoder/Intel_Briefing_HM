# 每日商业情报简报: 2026-05-11


**日期:** 2026-05-11
**生成时间:** 01:30
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [bytedance/UI-TARS-desktop - The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra](https://github.com/bytedance/UI-TARS-desktop)
📍 GitHub | 🔥 32,153 stars | 🕒 Today

### 2. [anthropics/financial-services - ](https://github.com/anthropics/financial-services)
📍 GitHub | 🔥 18,871 stars | 🕒 Today

### 3. [addyosmani/agent-skills - Production-grade engineering skills for AI coding agents.](https://github.com/addyosmani/agent-skills)
📍 GitHub | 🔥 38,458 stars | 🕒 Today

### 4. [CloakHQ/CloakBrowser - Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed.](https://github.com/CloakHQ/CloakBrowser)
📍 GitHub | 🔥 4,755 stars | 🕒 Today

### 5. [HKUDS/AI-Trader - "AI-Trader: 100% Fully-Automated Agent-Native Trading"](https://github.com/HKUDS/AI-Trader)
📍 GitHub | 🔥 15,589 stars | 🕒 Today

### 6. [jundot/omlx - LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar](https://github.com/jundot/omlx)
📍 GitHub | 🔥 13,307 stars | 🕒 Today

### 7. [datawhalechina/easy-vibe - 💻 vibe coding 2026 | Your first modern Coding course for beginners to master step by step.](https://github.com/datawhalechina/easy-vibe)
📍 GitHub | 🔥 9,186 stars | 🕒 Today

### 8. [playcanvas/supersplat - 3D Gaussian Splat Editor](https://github.com/playcanvas/supersplat)
📍 GitHub | 🔥 6,829 stars | 🕒 Today

### 9. [lsdefine/GenericAgent - Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption](https://github.com/lsdefine/GenericAgent)
📍 GitHub | 🔥 10,534 stars | 🕒 Today

### 10. [decolua/9router - Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini via 40+ providers. Auto-fallback, RTK -40% tokens, never hit limits.](https://github.com/decolua/9router)
📍 GitHub | 🔥 7,312 stars | 🕒 Today

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [沪指开盘突破4200点](https://wallstreetcn.com/articles/3771947)
📍 WallStreetCN | 🕒 01:27

### 2. [美国总统特朗普将对中国进行国事访问](https://wallstreetcn.com/articles/3771944)
📍 WallStreetCN | 🕒 01:02

### 3. [除了算力，还能买什么？](https://wallstreetcn.com/articles/3771943)
📍 WallStreetCN | 🕒 00:46

### 4. [北美数据中心史上最紧张供应：土、电、水、光全面短缺！](https://wallstreetcn.com/member/articles/3771573)
📍 WallStreetCN | 🕒 00:40

### 5. [美伊局势再度紧张，油价跳涨、黄金下跌，AI浪潮下韩股涨超4%，SK海力士涨10%、三星再创新高](https://wallstreetcn.com/articles/3771942)
📍 WallStreetCN | 🕒 00:37

### 6. [牵动全球市场的关键问题：伊朗危机走向何方？](https://wallstreetcn.com/themes/1008388)
📍 WallStreetCN | 🕒 

### 7. [申万宏源：A 股赚钱效应正质变，增量资金正循环的条件已具备](https://wallstreetcn.com/articles/3771941)
📍 WallStreetCN | 🕒 00:34

### 8. [伊朗回应“提议30天内撤销石油制裁”，特朗普称“完全不可接受”，内塔尼亚胡“美以对伊朗的军事行动尚未结束”](https://wallstreetcn.com/articles/3771940)
📍 WallStreetCN | 🕒 00:22

### 9. [差一点点“反超英伟达”！谷歌距离“全球第一市值”一步之遥](https://wallstreetcn.com/articles/3771937)
📍 WallStreetCN | 🕒 00:09

### 10. [报道：投资者热捧，“热门芯片新股”Cerebras考虑大幅上调IPO定价区间](https://wallstreetcn.com/articles/3771939)
📍 WallStreetCN | 🕒 00:09

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
🔥 746 votes

### 3. [Clera](https://www.producthunt.com/posts/clera)
> An AI agent matching candidates to the right roles.
🔥 715 votes

### 4. [Kilo Code v7 for VS Code](https://www.producthunt.com/posts/kilo-code-v7-for-vs-code)
> Parallel agents, diff reviewer, and multi-model comparisons
🔥 635 votes

### 5. [Dune](https://www.producthunt.com/posts/dune-5)
> Context-aware Mac keypad to automate workflows + meetings
🔥 634 votes

### 6. [Open Wearables](https://www.producthunt.com/posts/open-wearables-3)
> Open infrastructure for wearable-powered health products.
🔥 630 votes

### 7. [RankAI](https://www.producthunt.com/posts/rankai-2)
> RankAI autonomously gets you buyers from Google & AI Search
🔥 604 votes

### 8. [RankSpot](https://www.producthunt.com/posts/rankspot)
> AI SEO Blog driven by deep competitor intelligence
🔥 594 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [女朋友怀孕了，要还是不要](https://www.v2ex.com/t/1211648)
💬 111 replies

### 2. [我有一招可以在裁员潮的当下反击你的老板，并提高自身竞争力。](https://www.v2ex.com/t/1211625)
💬 67 replies

### 3. [安卓 17 没人讨论吗？要出 PC 桌面模式了](https://www.v2ex.com/t/1211669)
💬 51 replies

### 4. [Deekseek v4 真不错，一天时间写了一个 rust 的 trojan 的服务端](https://www.v2ex.com/t/1211677)
💬 43 replies

### 5. [老问我失业 1 年怎么活的吗，给你们分享下 深圳低成本生存指南（2026 年实测版）](https://www.v2ex.com/t/1211699)
💬 42 replies

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

### 3. [The left-wing case for AI](https://seangoedecke.com/the-left-wing-case-for-ai/)
📍 seangoedecke.com | 📅 Sun, 10 May 2026

### 4. [AI makes weak engineers less harmful](https://seangoedecke.com/ai-makes-weak-engineers-less-harmful/)
📍 seangoedecke.com | 📅 Sat, 09 May 2026

### 5. [Canvas Breach Disrupts Schools & Colleges Nationwide](https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/)
📍 krebsonsecurity.com | 📅 Fri, 08 May 2026

---
*报告由 Unified Intelligence Engine V2 自动生成*