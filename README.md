<h1 align="center">Rayân Mouahid</h1>

<p align="center">
  Engineering student at CY Tech, looking for an AI engineering internship from March 2027.<br>
  I build retrieval and agent systems end to end, and I measure them: every figure below comes from a script in its repository.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/rmouahid">LinkedIn</a> ·
  <a href="mailto:prorayanmouahid@gmail.com">prorayanmouahid@gmail.com</a> ·
  <a href="https://docs.google.com/document/d/1AUHSf6siZ9bExP_u02Gcvrgx173s5qi34O4Ov_In1m8/export?format=pdf">CV</a>
</p>

---

### [rag-agent](https://github.com/rmouahid/rag-agent): vector search written from scratch, measured against FAISS

<table>
<tr>
<td width="55%" valign="top">
<a href="https://github.com/rmouahid/rag-agent"><img src="https://raw.githubusercontent.com/rmouahid/rag-agent/main/docs/benchmarks/sift_recall_latency.png" alt="Recall@10 against query latency for each vector index on 100,000 SIFT1M vectors"></a>
</td>
<td valign="top">

A question-answering agent over your own documents. IVF, HNSW and product quantization are written in numpy, the answers come from a local LLM (llama.cpp), and everything is benchmarked on public datasets.

**432×** faster than an exact scan at recall@10 0.93 on 100,000 chunks ([scale study](https://github.com/rmouahid/rag-agent/blob/main/docs/benchmarks/scale.md))<br>
**0.668** nDCG@10 on BEIR SciFact ([report](https://github.com/rmouahid/rag-agent/blob/main/docs/benchmarks/beir_scifact.md))

`Python` `numpy` `FAISS` `FastAPI` `llama.cpp` `Docker`

</td>
</tr>
</table>

### [intern-radar](https://github.com/rmouahid/intern-radar): an internship watcher that runs every day on a VPS

<table>
<tr>
<td width="55%" valign="top">
<a href="https://github.com/rmouahid/intern-radar"><img src="https://raw.githubusercontent.com/rmouahid/intern-radar/develop/docs/metrics.svg" alt="New internship postings per day over 30 days, split between those removed by rules and those sent to the LLM"></a>
</td>
<td valign="top">

Watches the career pages of 119 companies, filters each new internship offer with rules and then an LLM, sends the relevant ones to Telegram and writes a cover letter as a PDF on demand.

**103** new offers a day screened for **$0.15** a day, notification **3 min** after detection (median, [metrics](https://github.com/rmouahid/intern-radar/blob/develop/docs/metrics.md))

`Python` `httpx` `SQLite` `LLM` `systemd` `Docker`

</td>
</tr>
</table>

### [NovIT](https://github.com/rmouahid/NovIT): the day's tech news inside Claude, through MCP

<table>
<tr>
<td width="55%" valign="top">
<a href="https://github.com/rmouahid/NovIT"><img src="https://raw.githubusercontent.com/rmouahid/NovIT/main/docs/assets/demo.gif" alt="Real MCP session: the client starts NovIT over stdio and queries the live sources"></a>
</td>
<td valign="top">

An MCP server that collects 19 open sources (AI, security, engineering, regulation), ranks them for the user's profile and returns structured, citable answers to Claude or any MCP client.

**19** sources collected in **2.0 s** ([profiling script](https://github.com/rmouahid/NovIT/blob/main/scripts/profile_scrapers.py)), **352** tests including a real MCP client over stdio

`Python` `MCP` `SQLite FTS5` `asyncio` `Docker`

</td>
</tr>
</table>
