# 每日商业情报简报: 2026-06-25


**日期:** 2026-06-25
**生成时间:** 01:50
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [OpenAI unveils its first custom chip, built by Broadcom](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)
📍 Hacker News | 🔥 523 points | 🕒 8 hours ago

### 2. [LuaJIT 3.0 proposed syntax extensions](https://github.com/LuaJIT/LuaJIT/issues/1475)
📍 Hacker News | 🔥 39 points | 🕒 1 hour ago

### 3. [Blogging can just be stating the obvious](https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/)
📍 Hacker News | 🔥 64 points | 🕒 2 hours ago

### 4. [Qualcomm to Acquire Modular](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/)
📍 Hacker News | 🔥 142 points | 🕒 5 hours ago

### 5. [Dostoyevsky isn't difficult](https://www.autodidacts.io/dostoyevsky-isnt-difficult/)
📍 Hacker News | 🔥 26 points | 🕒 2 hours ago

### 6. [Ending All Respiratory Infections](https://blog.interceptfund.com/p/ending-respiratory-infections)
📍 Hacker News | 🔥 8 points | 🕒 34 minutes ago

### 7. [RubyLLM: A Ruby framework for all major AI providers](https://rubyllm.com/)
📍 Hacker News | 🔥 346 points | 🕒 11 hours ago

### 8. [PR spam today looks like email spam in the early 2000s](https://www.greptile.com/blog/prs-on-openclaw)
📍 Hacker News | 🔥 180 points | 🕒 10 hours ago

### 9. [Computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)
📍 Hacker News | 🔥 170 points | 🕒 8 hours ago

### 10. [45°C cooling design cuts data center water use to near zero](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/)
📍 Hacker News | 🔥 192 points | 🕒 11 hours ago

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [美股狂飙，美元为何没跟上？](https://wallstreetcn.com/articles/3775464)
📍 WallStreetCN | 🕒 01:46

### 2. [日本酸素官宣提价30%开启新一轮涨价潮，氦气正升格为半导体产业链“卡脖子”级别战略物资](https://wallstreetcn.com/member/articles/3775266)
📍 WallStreetCN | 🕒 01:44

### 3. [创业板指涨超1%。科创50指数涨超1%，首次突破2000点，年内累计涨近50%](https://wallstreetcn.com/articles/3775467)
📍 WallStreetCN | 🕒 01:37

### 4. [科济药业拿下全球首款实体瘤CAR-T ，一针99万迎商业化大考](https://wallstreetcn.com/articles/3775466)
📍 WallStreetCN | 🕒 01:32

### 5. [康宁推出玻璃光学互连技术，剑指CPO市场](https://wallstreetcn.com/articles/3775461)
📍 WallStreetCN | 🕒 01:30

### 6. [美法案迫使盟友限制对华出口，荷兰不满，与美在“低端设备限制存分歧”](https://wallstreetcn.com/articles/3775462)
📍 WallStreetCN | 🕒 01:30

### 7. [铠侠年报里的“存储超级周期”：苹果订单暴增、原料库存激增，整条产业链都在抢先布局](https://wallstreetcn.com/articles/3775460)
📍 WallStreetCN | 🕒 01:27

### 8. [2.99万，买吗？](https://wallstreetcn.com/charts/41959298)
📍 WallStreetCN | 🕒 01:27

### 9. [中国央行：将在6月29日、6月30日公开市场操作中增加隔夜逆回购操作品种](https://wallstreetcn.com/livenews/3124327)
📍 WallStreetCN | 🕒 01:04

### 10. [摩根大通领衔，美国大行通过压力测试后掀起分红潮](https://wallstreetcn.com/articles/3775457)
📍 WallStreetCN | 🕒 00:43

## 📚 学术前沿 (Research)
> ArXiv AI/ML Papers

### 1. [InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884v1)
> ⚡ Vision-language-action (VLA) models can learn manipulation skills from demonstra...
👤 Maggie Wang, Lars Osterberg | 📅 2026-06-23

**详情:** Vision-language-action (VLA) models can learn manipulation skills from demonstrations, but their capabilities are bounded by the skills in the training data. We present InSight, a framework that unlocks autonomous skill acquisition by rendering VLAs steerable at the primitive-action level (e.g., "move gripper to the bowl", "lift upward", "pour the bottle"). InSight consists of two primary stages: (1) an automated segmentation pipeline that partitions demonstrations into labeled primitives via VLM plan decomposition and end-effector poses to enable VLA primitive steerability, and (2) a VLM-guided data flywheel that identifies missing primitives required to accomplish a novel task, autonomously attempts demonstrations of the missing primitives with VLM-proposed low-level control, and automatically labels, stores, and integrates successful demonstrations into the VLA training set. We evaluate InSight across simulation and real-world manipulation tasks, including block flipping, drawer closing, sweeping, twisting, and pouring, without any human demonstrations of these target skills. Once learned, these primitives can be composed to execute novel, long-horizon tasks without additional human demonstrations. Our findings demonstrate that primitive steerability provides a practical foundation for continual skill acquisition in VLA policies. Project website: https://insight-vla.github.io.

### 2. [FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation](https://arxiv.org/abs/2606.24874v1)
> ⚡ Sparse voxel representation has emerged as a scalable foundation for image-to-3D...
👤 Haorui Ji, Weizhe Liu | 📅 2026-06-23

**详情:** Sparse voxel representation has emerged as a scalable foundation for image-to-3D Gaussian Splatting (3DGS) generation, yet current methods struggle to preserve high-frequency visual details of input images due to two structural bottlenecks. First, they adopt discriminative 2D features optimized for semantic abstraction to construct sparse voxel latents, which suppress reconstructive cues and induce a representation bottleneck. Second, in the generation stage, standard diffusion transformers lack effective mechanisms to align dense 2D image tokens with sparse 3D voxel latents, resulting in a cross-modal correspondence bottleneck. To address these issues, we propose FLUX3D, a scalable image-to-3DGS framework that boosts both representation learning and cross-modal alignment during generation. We first revisit 2D feature selection for sparse-voxel-based 3D representation learning, propose Diffusion-Aligned Structured Latents (DA-SLAT) and couple it with a decoder-only architecture to improve 3DGS reconstruction fidelity. We also design a sparse-structure-aware diffusion framework, which integrates the Sparse-structure Multimodal Diffusion Transformer (SMDiT) and Modal-Aware Rotary Positional Embedding (MARoPE) to achieve geometry-agnostic 2D-3D alignment. Extensive benchmark experiments demonstrate that FLUX3D yields substantial improvements in appearance fidelity and significantly outperforms all state-of-the-art (SOTA) methods in generating high-quality 3DGS assets.

### 3. [OpenThoughts-Agent: Data Recipes for Agentic Models](https://arxiv.org/abs/2606.24855v1)
> ⚡ Agentic language models dramatically expand the applications of AI yet little is...
👤 Negin Raoof, Richard Zhuang | 📅 2026-06-23

**详情:** Agentic language models dramatically expand the applications of AI yet little is publicly known about how to curate training data for broadly capable agents. Existing open efforts such as SWE-Smith, SERA, and Nemotron-Terminal typically target a single benchmark, leaving open the question of how to train models that generalize across diverse agentic tasks. The OpenThoughts-Agent (OT-Agent) project addresses this gap with a fully open data curation pipeline for training agentic models. We conduct more than 100 controlled ablation experiments to systematically investigate each stage of the pipeline, yielding insights on the importance of task sources and diversity. We then assemble a training set of 100K examples from our pipeline and fine-tune Qwen3-32B on this dataset, which yields an average accuracy of 44.8% across seven agentic benchmarks and a 3.9 percentage point improvement over the strongest existing open data agentic model (Nemotron-Terminal-32B, 40.9%). Moreover, our training data exhibits strong scaling properties, outperforming alternative open datasets at every training set size in compute-controlled comparisons. We publicly release our training sets, data pipeline, experimental data, and models at openthoughts.ai to support future open research on agentic model training.

### 4. [It's Complicated: On the Design and Evaluation of AI-Powered AAC Interfaces](https://arxiv.org/abs/2606.24854v1)
> ⚡ Artificial intelligence (AI) can enhance what people who use augmentative and al...
👤 Blade Frisch, Will Wade | 📅 2026-06-23

**详情:** Artificial intelligence (AI) can enhance what people who use augmentative and alternative communication (AAC) are able to do with their systems. However, evaluating AI-powered AAC interfaces can be difficult. People are intersectional beings and current evaluation metrics can struggle to capture the multifaceted and nuanced desires people may have for their AAC. We explore the complicated nature of six AAC problem spaces, explore how AI might be used in these spaces, and suggest more robust methods of evaluation that take the intersectional nuances of people into account. We also discuss broader issues that arise across these problem spaces and how they could be addressed using our proposed evaluation methods.

### 5. [IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation](https://arxiv.org/abs/2606.24849v1)
> ⚡ Unified multi-modal large language models (MLLMs) have achieved strong text-to-i...
👤 Zixuan Li, Haokun Lin | 📅 2026-06-23

**详情:** Unified multi-modal large language models (MLLMs) have achieved strong text-to-image generation quality, but still struggle with structure-aware prompt following, where object counts, spatial relations, attribute bindings, and coarse layouts must be preserved. We attribute this limitation in part to the entanglement of structural planning and appearance rendering within a single conditioning stream. To address this issue, we propose Implicit Visual Chain-of-Thought (IV-CoT), a latent visual reasoning framework for query-conditioned image generation. IV-CoT decomposes the visual conditioning queries into a structural-to-semantic cascade, where structural queries first form a latent visual plan and semantic queries then render appearance conditioned on this plan. To guide the structural queries, we introduce training-only sketch supervision, which encourages them to capture structure from sketches without requiring sketch extraction or intermediate decoding at inference time. IV-CoT performs implicit CoT reasoning in a single forward pass and achieves superior results on GenEval and T2I-CompBench. Visualizations and analyses demonstrate that the learned structural and semantic queries play complementary roles in structure-aware generation.

## 💎 产品精选 (Product Gems)
> Product Hunt Today

### 1. [Fundraisly](https://www.producthunt.com/posts/fundraisly-4)
> AI fundraising agent that finds investors and books meetings
🔥 1438 votes

### 2. [Brew ](https://www.producthunt.com/posts/brew-4)
> Like Claude design for email marketing
🔥 962 votes

### 3. [Upstream](https://www.producthunt.com/posts/upstream-5)
> The inbox designed for humans and agents
🔥 876 votes

### 4. [Goldfish](https://www.producthunt.com/posts/goldfish)
> Press Option. It knows your work and replies like you
🔥 873 votes

### 5. [Unabyss](https://www.producthunt.com/posts/unabyss)
> MCP-native self-updating context layer for your AI
🔥 791 votes

### 6. [Bond](https://www.producthunt.com/posts/bond-717)
> The AI to-do list that does itself
🔥 755 votes

### 7. [Mailwarm 2.0](https://www.producthunt.com/posts/mailwarm-2-0)
> The email warmup tool, upgraded for deliverability.
🔥 692 votes

### 8. [own.page](https://www.producthunt.com/posts/own-page)
> Make your own personal website with bento tiles
🔥 688 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [庆祝 Steam Machine 发布，再送一台价值 5499 元懒猫微服！](https://www.v2ex.com/t/1222480)
💬 256 replies

### 2. [Xiaomi 智能存储(NAS)开启众筹， 4TB 2299 起](https://www.v2ex.com/t/1222453)
💬 191 replies

### 3. [AndroMeld：在 Mac 上无缝操控你的 Android [送码]](https://www.v2ex.com/t/1222477)
💬 106 replies

### 4. [18cm 们，你们的车内有异响吗？](https://www.v2ex.com/t/1222438)
💬 94 replies

### 5. [[超稳定] 一个真正一目了然的自建 Codex 中转站](https://www.v2ex.com/t/1222511)
💬 89 replies

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

### 1. [Framework's 10G Ethernet module exposes USB-C's complexity](https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/)
📍 jeffgeerling.com | 📅 Wed, 24 Jun 2026

### 2. [You can finally power on a Mac remotely](https://www.jeffgeerling.com/blog/2026/power-on-your-mac-remotely/)
📍 jeffgeerling.com | 📅 Fri, 12 Jun 2026

### 3. [AI GPUs probably live longer than three years](https://seangoedecke.com/ai-gpus-live-longer-than-three-years/)
📍 seangoedecke.com | 📅 Mon, 15 Jun 2026

### 4. [Working with product managers](https://seangoedecke.com/working-with-product-managers/)
📍 seangoedecke.com | 📅 Mon, 08 Jun 2026

### 5. [Scattered Spider Hackers Plead Guilty on Day 1 of Trial](https://krebsonsecurity.com/2026/06/scattered-spider-hackers-plead-guilty-on-day-1-of-trial/)
📍 krebsonsecurity.com | 📅 Tue, 23 Jun 2026

---
*报告由 Unified Intelligence Engine V2 自动生成*