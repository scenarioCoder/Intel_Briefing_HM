# 每日商业情报简报: 2026-03-18


**日期:** 2026-03-18
**生成时间:** 00:03
**数据源:** HN, GitHub, 36Kr, WallStreetCN, V2EX, PH, ArXiv, X, XHS

---

## 🛠️ 技术趋势 (Tech Trends)
> Hacker News + GitHub Trending

### 1. [A Decade of Slug](https://terathon.com/blog/decade-slug.html)
📍 Hacker News | 🔥 363 points | 🕒 5 hours ago

### 2. [Python 3.15's JIT is now back on track](https://fidget-spinner.github.io/posts/jit-on-track.html)
📍 Hacker News | 🔥 228 points | 🕒 5 hours ago

### 3. [Get Shit Done: A Meta-Prompting, Context Engineering and Spec-Driven Dev System](https://github.com/gsd-build/get-shit-done)
📍 Hacker News | 🔥 148 points | 🕒 3 hours ago

### 4. [Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'](https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level)
📍 Hacker News | 🔥 485 points | 🕒 8 hours ago

### 5. [It Took Me 30 Years to Solve This VFX Problem – Green Screen Problem [video]](https://www.youtube.com/watch?v=3Ploi723hg4)
📍 Hacker News | 🔥 141 points | 🕒 6 hours ago

### 6. [Kagi Small Web](https://kagi.com/smallweb/)
📍 Hacker News | 🔥 683 points | 🕒 14 hours ago

### 7. [Mistral AI Releases Forge](https://mistral.ai/news/forge)
📍 Hacker News | 🔥 55 points | 🕒 2 hours ago

### 8. [Launch HN: Kita (YC W26) – Automate credit review in emerging markets](https://news.ycombinator.com/item?id=47417335)
📍 Hacker News | 🔥 21 points | 🕒 2 hours ago

### 9. [Torturing Rustc by Emulating HKTs](https://www.harudagondi.space/blog/torturing-rustc-by-emulating-hkts/)
📍 Hacker News | 🔥 42 points | 🕒 4 hours ago

### 10. [Unsloth Studio](https://unsloth.ai/docs/new/studio)
📍 Hacker News | 🔥 124 points | 🕒 8 hours ago

## 💰 资本动向 (Capital Flow)
> 36Kr + 华尔街见闻

### 1. [伊朗总统证实：拉里贾尼遇袭身亡！儿子与副手一同遇害，以色列对其进行了数周跟踪，内塔尼亚胡：后续会有更多“惊喜”](https://wallstreetcn.com/articles/3767776)
📍 WallStreetCN | 🕒 23:57

### 2. [罕见的看空黄金报告：5000美元金价太高，堪比1980年和2011年高点](https://wallstreetcn.com/articles/3767772)
📍 WallStreetCN | 🕒 23:52

### 3. [首位辞职高官！美国家反恐中心主任辞职：无法昧着良心支持对伊朗战争](https://wallstreetcn.com/articles/3767774)
📍 WallStreetCN | 🕒 23:49

### 4. [3月18日会员早报：美联储议息会议重磅前瞻，半导体涨价潮来袭](https://wallstreetcn.com/member/articles/3767773)
📍 WallStreetCN | 🕒 23:32

### 5. [华尔街见闻早餐FM-Radio | 2026年3月18日](https://wallstreetcn.com/articles/3767771)
📍 WallStreetCN | 🕒 23:20

### 6. [牵动全球市场的关键问题：伊朗危机走向何方？](https://wallstreetcn.com/themes/1008388)
📍 WallStreetCN | 🕒 

### 7. [静待美联储决议，股油同涨，美债走强，美元两连跌，黄金连续两日持稳于5000关口](https://wallstreetcn.com/articles/3767701)
📍 WallStreetCN | 🕒 23:00

### 8. [“新美联储通讯社”：从"何时降息"到"是否降息"，关注三大信号窗口](https://wallstreetcn.com/articles/3767770)
📍 WallStreetCN | 🕒 22:21

### 9. [特朗普称对伊行动无需北约和日韩澳帮助，伊朗宣告打击进入"加速阶段"、总统证实拉里贾尼身亡](https://wallstreetcn.com/articles/3767756)
📍 WallStreetCN | 🕒 22:10

### 10. [伊朗：拉里贾尼儿子和副手一同遭空袭身亡](https://wallstreetcn.com/livenews/3071931)
📍 WallStreetCN | 🕒 22:05

## 📚 学术前沿 (Research)
> ArXiv AI/ML Papers

### 1. [Mixture-of-Depths Attention](https://arxiv.org/abs/2603.15619v1)
> ⚡ Scaling depth is a key driver for large language models (LLMs). Yet, as LLMs bec...
👤 Lianghui Zhu, Yuxin Fang | 📅 2026-03-16

**详情:** Scaling depth is a key driver for large language models (LLMs). Yet, as LLMs become deeper, they often suffer from signal degradation: informative features formed in shallow layers are gradually diluted by repeated residual updates, making them harder to recover in deeper layers. We introduce mixture-of-depths attention (MoDA), a mechanism that allows each attention head to attend to sequence KV pairs at the current layer and depth KV pairs from preceding layers. We further describe a hardware-efficient algorithm for MoDA that resolves non-contiguous memory-access patterns, achieving 97.3% of FlashAttention-2's efficiency at a sequence length of 64K. Experiments on 1.5B-parameter models demonstrate that MoDA consistently outperforms strong baselines. Notably, it improves average perplexity by 0.2 across 10 validation benchmarks and increases average performance by 2.11% on 10 downstream tasks, with a negligible 3.7% FLOPs computational overhead. We also find that combining MoDA with post-norm yields better performance than using it with pre-norm. These results suggest that MoDA is a promising primitive for depth scaling. Code is released at https://github.com/hustvl/MoDA .

### 2. [Mechanistic Origin of Moral Indifference in Language Models](https://arxiv.org/abs/2603.15615v1)
> ⚡ Existing behavioral alignment techniques for Large Language Models (LLMs) often ...
👤 Lingyu Li, Yan Teng | 📅 2026-03-16

**详情:** Existing behavioral alignment techniques for Large Language Models (LLMs) often neglect the discrepancy between surface compliance and internal unaligned representations, leaving LLMs vulnerable to long-tail risks. More crucially, we posit that LLMs possess an inherent state of moral indifference due to compressing distinct moral concepts into uniform probability distributions. We verify and remedy this indifference in LLMs' latent representations, utilizing 251k moral vectors constructed upon Prototype Theory and the Social-Chemistry-101 dataset. Firstly, our analysis across 23 models reveals that current LLMs fail to represent the distinction between opposed moral categories and fine-grained typicality gradients within these categories; notably, neither model scaling, architecture, nor explicit alignment reshapes this indifference. We then employ Sparse Autoencoders on Qwen3-8B, isolate mono-semantic moral features, and targetedly reconstruct their topological relationships to align with ground-truth moral vectors. This representational alignment naturally improves moral reasoning and granularity, achieving a 75% pairwise win-rate on the independent adversarial Flames benchmark. Finally, we elaborate on the remedial nature of current intervention methods from an experientialist philosophy, arguing that endogenously aligned AI might require a transformation from post-hoc corrections to proactive cultivation.

### 3. [Do Metrics for Counterfactual Explanations Align with User Perception?](https://arxiv.org/abs/2603.15607v1)
> ⚡ Explainability is widely regarded as essential for trustworthy artificial intell...
👤 Felix Liedeker, Basil Ell | 📅 2026-03-16

**详情:** Explainability is widely regarded as essential for trustworthy artificial intelligence systems. However, the metrics commonly used to evaluate counterfactual explanations are algorithmic evaluation metrics that are rarely validated against human judgments of explanation quality. This raises the question of whether such metrics meaningfully reflect user perceptions. We address this question through an empirical study that directly compares algorithmic evaluation metrics with human judgments across three datasets. Participants rated counterfactual explanations along multiple dimensions of perceived quality, which we relate to a comprehensive set of standard counterfactual metrics. We analyze both individual relationships and the extent to which combinations of metrics can predict human assessments. Our results show that correlations between algorithmic metrics and human ratings are generally weak and strongly dataset-dependent. Moreover, increasing the number of metrics used in predictive models does not lead to reliable improvements, indicating structural limitations in how current metrics capture criteria relevant for humans. Overall, our findings suggest that widely used counterfactual evaluation metrics fail to reflect key aspects of explanation quality as perceived by users, underscoring the need for more human-centered approaches to evaluating explainable artificial intelligence.

### 4. [From Passive Observer to Active Critic: Reinforcement Learning Elicits Process Reasoning for Robotic Manipulation](https://arxiv.org/abs/2603.15600v1)
> ⚡ Accurate process supervision remains a critical challenge for long-horizon robot...
👤 Yibin Liu, Yaxing Lyu | 📅 2026-03-16

**详情:** Accurate process supervision remains a critical challenge for long-horizon robotic manipulation. A primary bottleneck is that current video MLLMs, trained primarily under a Supervised Fine-Tuning (SFT) paradigm, function as passive "Observers" that recognize ongoing events rather than evaluating the current state relative to the final task goal. In this paper, we introduce PRIMO R1 (Process Reasoning Induced Monitoring), a 7B framework that transforms video MLLMs into active "Critics". We leverage outcome-based Reinforcement Learning to incentivize explicit Chain-of-Thought generation for progress estimation. Furthermore, our architecture constructs a structured temporal input by explicitly anchoring the video sequence between initial and current state images. Supported by the proposed PRIMO Dataset and Benchmark, extensive experiments across diverse in-domain environments and out-of-domain real-world humanoid scenarios demonstrate that PRIMO R1 achieves state-of-the-art performance. Quantitatively, our 7B model achieves a 50% reduction in the mean absolute error of specialized reasoning baselines, demonstrating significant relative accuracy improvements over 72B-scale general MLLMs. Furthermore, PRIMO R1 exhibits strong zero-shot generalization on difficult failure detection tasks. We establish state-of-the-art performance on RoboFail benchmark with 67.0% accuracy, surpassing closed-source models like OpenAI o1 by 6.0%.

### 5. [OpenSeeker: Democratizing Frontier Search Agents by Fully Open-Sourcing Training Data](https://arxiv.org/abs/2603.15594v1)
> ⚡ Deep search capabilities have become an indispensable competency for frontier La...
👤 Yuwen Du, Rui Ye | 📅 2026-03-16

**详情:** Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet the development of high-performance search agents remains dominated by industrial giants due to a lack of transparent, high-quality training data. This persistent data scarcity has fundamentally hindered the progress of the broader research community in developing and innovating within this domain. To bridge this gap, we introduce OpenSeeker, the first fully open-source search agent (i.e., model and data) that achieves frontier-level performance through two core technical innovations: (1) Fact-grounded scalable controllable QA synthesis, which reverse-engineers the web graph via topological expansion and entity obfuscation to generate complex, multi-hop reasoning tasks with controllable coverage and complexity. (2) Denoised trajectory synthesis, which employs a retrospective summarization mechanism to denoise the trajectory, therefore promoting the teacher LLMs to generate high-quality actions. Experimental results demonstrate that OpenSeeker, trained (a single training run) on only 11.7k synthesized samples, achieves state-of-the-art performance across multiple benchmarks including BrowseComp, BrowseComp-ZH, xbench-DeepSearch, and WideSearch. Notably, trained with simple SFT, OpenSeeker significantly outperforms the second-best fully open-source agent DeepDive (e.g., 29.5% v.s. 15.3% on BrowseComp), and even surpasses industrial competitors such as Tongyi DeepResearch (trained via extensive continual pre-training, SFT, and RL) on BrowseComp-ZH (48.4% v.s. 46.7%). We fully open-source the complete training dataset and the model weights to democratize frontier search agent research and foster a more transparent, collaborative ecosystem.

## 💎 产品精选 (Product Gems)
> Product Hunt Today

### 1. [Rork Max](https://www.producthunt.com/posts/rork-max)
> Best AI for iOS apps. Website that replaces Xcode
🔥 1466 votes

### 2. [KiloClaw](https://www.producthunt.com/posts/kiloclaw)
> Hosted OpenClaw. No Mac mini required.
🔥 876 votes

### 3. [Visual Translate by Vozo](https://www.producthunt.com/posts/visual-translate-by-vozo)
> Translate text in your videos without recreating visuals
🔥 735 votes

### 4. [Sonnet 4.6](https://www.producthunt.com/posts/sonnet-4-6)
> The most capable Sonnet model yet
🔥 731 votes

### 5. [Chronicle 2.0](https://www.producthunt.com/posts/chronicle-2-0)
> AI presentations without the AI slop
🔥 720 votes

### 6. [Claude Import Memory](https://www.producthunt.com/posts/claude-import-memory)
> Switch from ChatGPT to Claude with import memory feature
🔥 696 votes

### 7. [Stitch by Google](https://www.producthunt.com/posts/stitch-by-google)
> Turn napkin sketches into production-ready UI in seconds.
🔥 664 votes

### 8. [Naoma AI Demo Agent](https://www.producthunt.com/posts/naoma-ai-demo-agent)
> The video AI demo agent for B2B SaaS for immediate demos
🔥 661 votes

## 🐦 社交热议 (Social)
> X (Twitter) - AI/Tech Discussions

*暂无数据 (需要配置 XAI_API_KEY)*

## 🗣️ 社区热点 (Community)
> V2EX 热门

### 1. [五年谈的 4 个女朋友，给各位大佬一点借鉴，以及迷茫一下现在！](https://www.v2ex.com/t/1198831)
💬 158 replies

### 2. [出海/远程利器：任意输入框，中/英/混打随便写，免切屏一键润色成专业得体的母语级表达（送会员）](https://www.v2ex.com/t/1198813)
💬 124 replies

### 3. [目前智驾谁是中国第一？](https://www.v2ex.com/t/1198848)
💬 117 replies

### 4. [说说曾经买过的软件](https://www.v2ex.com/t/1198822)
💬 101 replies

### 5. [结婚选日子看八字很重要吗，为什么答案都不同？](https://www.v2ex.com/t/1198846)
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