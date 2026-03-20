# 每日商业情报简报: 2026-03-20


**日期:** 2026-03-20
**生成时间:** 00:01
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [opendataloader-project/opendataloader-pdf - PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.](https://github.com/opendataloader-project/opendataloader-pdf)
📍 GitHub | 🔥 5,545 stars | 🕒 Today

### 2. [langchain-ai/open-swe - An Open-Source Asynchronous Coding Agent](https://github.com/langchain-ai/open-swe)
📍 GitHub | 🔥 7,011 stars | 🕒 Today

### 3. [obra/superpowers - An agentic skills framework & software development methodology that works.](https://github.com/obra/superpowers)
📍 GitHub | 🔥 99,115 stars | 🕒 Today

### 4. [jarrodwatts/claude-hud - A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress](https://github.com/jarrodwatts/claude-hud)
📍 GitHub | 🔥 8,475 stars | 🕒 Today

### 5. [unslothai/unsloth - Unified web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.](https://github.com/unslothai/unsloth)
📍 GitHub | 🔥 56,682 stars | 🕒 Today

### 6. [mobile-dev-inc/Maestro - Painless E2E Automation for Mobile and Web](https://github.com/mobile-dev-inc/Maestro)
📍 GitHub | 🔥 12,419 stars | 🕒 Today

### 7. [newton-physics/newton - An open-source, GPU-accelerated physics simulation engine built upon NVIDIA Warp, specifically targeting roboticists and simulation researchers.](https://github.com/newton-physics/newton)
📍 GitHub | 🔥 3,216 stars | 🕒 Today

### 8. [louis-e/arnis - Generate any location from the real world in Minecraft with a high level of detail.](https://github.com/louis-e/arnis)
📍 GitHub | 🔥 10,727 stars | 🕒 Today

### 9. [FujiwaraChoki/MoneyPrinterV2 - Automate the process of making money online.](https://github.com/FujiwaraChoki/MoneyPrinterV2)
📍 GitHub | 🔥 16,042 stars | 🕒 Today

### 10. [gsd-build/get-shit-done - A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.](https://github.com/gsd-build/get-shit-done)
📍 GitHub | 🔥 36,061 stars | 🕒 Today

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [油价狂飙下的消费股危机：通胀粘性+需求疲软，美股消费板块将重演70年代剧本？](https://wallstreetcn.com/member/articles/3767902)
📍 WallStreetCN | 🕒 23:34

### 2. [华尔街见闻早餐FM-Radio | 2026年3月20日](https://wallstreetcn.com/articles/3767961)
📍 WallStreetCN | 🕒 23:31

### 3. [油价动荡主导市场，美股美债企稳，全球央行"鹰派按兵不动"，黄金一度暴跌6%](https://wallstreetcn.com/articles/3767876)
📍 WallStreetCN | 🕒 23:00

### 4. [美国参议员Warren就爱泼斯坦档案中提及沃什质询，要求后者回应](https://wallstreetcn.com/articles/3767960)
📍 WallStreetCN | 🕒 22:00

### 5. [黄仁勋：AI领袖应避免散布恐慌，看好Anthropic营收2030年破万亿](https://wallstreetcn.com/articles/3767958)
📍 WallStreetCN | 🕒 21:50

### 6. [牵动全球市场的关键问题：伊朗危机走向何方？](https://wallstreetcn.com/themes/1008388)
📍 WallStreetCN | 🕒 

### 7. [油价拿住了美国的七寸：美国怕的不是经济衰退而是内部撕裂](https://wallstreetcn.com/member/articles/3767957)
📍 WallStreetCN | 🕒 21:50

### 8. [拉加德警告伊朗冲突对通胀构成实质性影响，呼吁政府应对能源危机时别用力过猛](https://wallstreetcn.com/articles/3767959)
📍 WallStreetCN | 🕒 21:41

### 9. [响应特朗普呼声，以色列总理称将暂停空袭伊朗能源设施，卡塔尔称伊袭破坏17%LNG产能](https://wallstreetcn.com/articles/3767948)
📍 WallStreetCN | 🕒 21:33

### 10. [伊朗称若基础设施再遭袭将不再克制、击中美F-35战机，美军或夺岛迫使伊开放霍尔木兹](https://wallstreetcn.com/articles/3767953)
📍 WallStreetCN | 🕒 21:04

## 📚 学术前沿 (Research)
> ArXiv AI/ML Papers

### 1. [Unified Spatio-Temporal Token Scoring for Efficient Video VLMs](https://arxiv.org/abs/2603.18004v1)
> ⚡ Token pruning is essential for enhancing the computational efficiency of vision-...
👤 Jianrui Zhang, Yue Yang | 📅 2026-03-18

**详情:** Token pruning is essential for enhancing the computational efficiency of vision-language models (VLMs), particularly for video-based tasks where temporal redundancy is prevalent. Prior approaches typically prune tokens either (1) within the vision transformer (ViT) exclusively for unimodal perception tasks such as action recognition and object segmentation, without adapting to downstream vision-language tasks; or (2) only within the LLM while leaving the ViT output intact, often requiring complex text-conditioned token selection mechanisms. In this paper, we introduce Spatio-Temporal Token Scoring (STTS), a simple and lightweight module that prunes vision tokens across both the ViT and the LLM without text conditioning or token merging, and is fully compatible with end-to-end training. By learning how to score temporally via an auxiliary loss and spatially via LLM downstream gradients, aided by our efficient packing algorithm, STTS prunes 50% of vision tokens throughout the entire architecture, resulting in a 62% improvement in efficiency during both training and inference with only a 0.7% drop in average performance across 13 short and long video QA tasks. Efficiency gains increase with more sampled frames per video. Applying test-time scaling for long-video QA further yields performance gains of 0.5-1% compared to the baseline. Overall, STTS represents a novel, simple yet effective technique for unified, architecture-wide vision token pruning.

### 2. [Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models](https://arxiv.org/abs/2603.18002v1)
> ⚡ Multimodal Large Language Models (MLLMs) have made impressive progress in connec...
👤 Kevin Qu, Haozhe Qi | 📅 2026-03-18

**详情:** Multimodal Large Language Models (MLLMs) have made impressive progress in connecting vision and language, but they still struggle with spatial understanding and viewpoint-aware reasoning. Recent efforts aim to augment the input representations with geometric cues rather than explicitly teaching models to reason in 3D space. We introduce Loc3R-VLM, a framework that equips 2D Vision-Language Models with advanced 3D understanding capabilities from monocular video input. Inspired by human spatial cognition, Loc3R-VLM relies on two joint objectives: global layout reconstruction to build a holistic representation of the scene structure, and explicit situation modeling to anchor egocentric perspective. These objectives provide direct spatial supervision that grounds both perception and language in a 3D context. To ensure geometric consistency and metric-scale alignment, we leverage lightweight camera pose priors extracted from a pre-trained 3D foundation model. Loc3R-VLM achieves state-of-the-art performance in language-based localization and outperforms existing 2D- and video-based approaches on situated and general 3D question-answering benchmarks, demonstrating that our spatial supervision framework enables strong 3D understanding. Project page: https://kevinqu7.github.io/loc3r-vlm

### 3. [AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse](https://arxiv.org/abs/2603.18000v1)
> ⚡ Building LLM-based agents has become increasingly important. Recent works on LLM...
👤 Zhang Zhang, Shuqi Lu | 📅 2026-03-18

**详情:** Building LLM-based agents has become increasingly important. Recent works on LLM-based agent self-evolution primarily record successful experiences as textual prompts or reflections, which cannot reliably guarantee efficient task re-execution in complex scenarios. We propose AgentFactory, a new self-evolution paradigm that preserves successful task solutions as executable subagent code rather than textual experience. Crucially, these subagents are continuously refined based on execution feedback, becoming increasingly robust and efficient as more tasks are encountered. Saved subagents are pure Python code with standardized documentation, enabling portability across any Python-capable system. We demonstrate that AgentFactory enables continuous capability accumulation: its library of executable subagents grows and improves over time, progressively reducing the effort required for similar tasks without manual intervention. Our implementation is open-sourced at https://github.com/zzatpku/AgentFactory, and our demonstration video is available at https://youtu.be/iKSsuAXJHW0.

### 4. [Toward Scalable Automated Repository-Level Datasets for Software Vulnerability Detection](https://arxiv.org/abs/2603.17974v1)
> ⚡ Software vulnerabilities continue to grow in volume and remain difficult to dete...
👤 Amine Lbath | 📅 2026-03-18

**详情:** Software vulnerabilities continue to grow in volume and remain difficult to detect in practice. Although learning-based vulnerability detection has progressed, existing benchmarks are largely function-centric and fail to capture realistic, executable, interprocedural settings. Recent repo-level security benchmarks demonstrate the importance of realistic environments, but their manual curation limits scale. This doctoral research proposes an automated benchmark generator that injects realistic vulnerabilities into real-world repositories and synthesizes reproducible proof-of-vulnerability (PoV) exploits, enabling precisely labeled datasets for training and evaluating repo-level vulnerability detection agents. We further investigate an adversarial co-evolution loop between injection and detection agents to improve robustness under realistic constraints.

### 5. [TDAD: Test-Driven Agentic Development - Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis](https://arxiv.org/abs/2603.17973v1)
> ⚡ AI coding agents can resolve real-world software issues, yet they frequently int...
👤 Pepe Alonso | 📅 2026-03-18

**详情:** AI coding agents can resolve real-world software issues, yet they frequently introduce regressions, breaking tests that previously passed. Current benchmarks focus almost exclusively on resolution rate, leaving regression behavior under-studied. This paper presents TDAD (Test-Driven Agentic Development), an open-source tool and benchmark methodology that combines abstract-syntax-tree (AST) based code-test graph construction with weighted impact analysis to surface the tests most likely affected by a proposed change. Evaluated on SWE-bench Verified with two local models (Qwen3-Coder 30B on 100 instances and Qwen3.5-35B-A3B on 25 instances), TDAD's GraphRAG workflow reduced test-level regressions by 70% (6.08% to 1.82%) and improved resolution from 24% to 32% when deployed as an agent skill. A surprising finding is that TDD prompting alone increased regressions (9.94%), revealing that smaller models benefit more from contextual information (which tests to verify) than from procedural instructions (how to do TDD). An autonomous auto-improvement loop raised resolution from 12% to 60% on a 10-instance subset with 0% regression. These findings suggest that for AI agent tool design, surfacing contextual information outperforms prescribing procedural workflows. All code, data, and logs are publicly available at https://github.com/pepealonso95/TDAD.

## 💎 产品精选 (Product Gems)
> Product Hunt Today

### 1. [Rork Max](https://www.producthunt.com/posts/rork-max)
> Best AI for iOS apps. Website that replaces Xcode
🔥 1470 votes

### 2. [KiloClaw](https://www.producthunt.com/posts/kiloclaw)
> Hosted OpenClaw. No Mac mini required.
🔥 880 votes

### 3. [Visual Translate by Vozo](https://www.producthunt.com/posts/visual-translate-by-vozo)
> Translate text in your videos without recreating visuals
🔥 741 votes

### 4. [Chronicle 2.0](https://www.producthunt.com/posts/chronicle-2-0)
> AI presentations without the AI slop
🔥 731 votes

### 5. [Claude Import Memory](https://www.producthunt.com/posts/claude-import-memory)
> Switch from ChatGPT to Claude with import memory feature
🔥 704 votes

### 6. [Anything API](https://www.producthunt.com/posts/anything-api)
> Any website. We deliver the API.
🔥 669 votes

### 7. [Stitch by Google](https://www.producthunt.com/posts/stitch-by-google)
> Turn napkin sketches into production-ready UI in seconds.
🔥 667 votes

### 8. [Naoma AI Demo Agent](https://www.producthunt.com/posts/naoma-ai-demo-agent)
> The video AI demo agent for B2B SaaS for immediate demos
🔥 664 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [没用过 opus4.6 + agents + skills + mcp 组合的人不足以谈 AI 编程](https://www.v2ex.com/t/1199424)
💬 146 replies

### 2. [你人生中最重要的事是什么呢？](https://www.v2ex.com/t/1199412)
💬 140 replies

### 3. [大家不要笑话我，最近突然觉得很绝望，不停在失业，找工作，写代码的循环中。](https://www.v2ex.com/t/1199457)
💬 124 replies

### 4. [有没有从 2030 年穿越回来的朋友，来点剧透？](https://www.v2ex.com/t/1199419)
💬 112 replies

### 5. [这个时代不适合结婚生子的理由是什么？](https://www.v2ex.com/t/1199503)
💬 110 replies

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

### 1. [Restoring an Xserve G5: When Apple built real servers](https://www.jeffgeerling.com/blog/2026/restoring-xserve-g5-apple-server/)
📍 jeffgeerling.com | 📅 Fri, 13 Mar 2026

### 2. [Can the MacBook Neo replace my M4 Air?](https://www.jeffgeerling.com/blog/2026/macbook-neo-replace-m4-air/)
📍 jeffgeerling.com | 📅 Thu, 12 Mar 2026

### 3. [Big tech engineers need big egos](https://seangoedecke.com/big-tech-needs-big-egos/)
📍 seangoedecke.com | 📅 Sat, 14 Mar 2026

### 4. [I don't know if my job will still exist in ten years](https://seangoedecke.com/will-my-job-still-exist/)
📍 seangoedecke.com | 📅 Fri, 06 Mar 2026

### 5. [Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker](https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker/)
📍 krebsonsecurity.com | 📅 Wed, 11 Mar 2026

---
*报告由 Unified Intelligence Engine V2 自动生成*