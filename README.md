<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0e17,50:0d2137,100:00d4ff&height=160&section=header&text=Kerem%20Apayd%C4%B1n&fontSize=42&fontColor=ffffff&fontAlignY=55&desc=Systems%20Programmer%20%C2%B7%20Embedded%20Linux%20%C2%B7%20Kernel%20Development&descAlignY=78&descSize=16" />

[![Email](https://img.shields.io/badge/apaydinkerem18%40gmail.com-0a0e17?style=flat-square&logo=gmail&logoColor=00d4ff)](mailto:apaydinkerem18@gmail.com)
[![LinkedIn](https://img.shields.io/badge/in-keremapaydin-0a0e17?style=flat-square&logoColor=00d4ff)](https://linkedin.com/in/keremapaydin)
[![GitHub](https://img.shields.io/badge/@livaiyena-0a0e17?style=flat-square&logo=github&logoColor=00d4ff)](https://github.com/livaiyena)

</div>

---

## `$ whoami`

Computer Engineering student specializing in **systems programming**, **embedded Linux**, and **software architecture**. I build low-level systems with a focus on concurrent I/O, kernel module development, and memory-optimal design — from custom kernel drivers to cross-compiled embedded environments, architecting complete systems end-to-end.

> *Kernel space to application layer. From bare metal to CI/CD pipeline.*

---

## `$ cat /proc/focus`

```
Current working area:  Embedded Systems & Kernel Development
Active target arch:    AArch64 (ARM64)
Primary language:      C
Build environment:     Docker / QEMU / Cross-toolchain (musl + gcc)
```

---

## `$ ls -la ~/projects/flagship/`

### [mini-linux](https://github.com/livaiyena/mini-linux) — Production-Grade Embedded Linux Telemetry System

> End-to-end embedded system: kernel driver → userspace IPC → minimal rootfs → automated CI/CD

![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![Linux](https://img.shields.io/badge/Linux_Kernel-FCC624?style=flat-square&logo=linux&logoColor=black)
![ARM64](https://img.shields.io/badge/ARM64-0091BD?style=flat-square&logo=arm&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![QEMU](https://img.shields.io/badge/QEMU-FF6600?style=flat-square&logo=qemu&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

<details>
<summary><b>▶ Full System Architecture</b></summary>

<br>

```
┌─────────────────────────────────────────────────────────────────┐
│                        mini-linux stack                         │
├─────────────────────────────────────────────────────────────────┤
│  [ Web Dashboard ]  BusyBox httpd + CGI  +  Gemini AI Diagnostics│
├─────────────────────────────────────────────────────────────────┤
│  [ Userspace ]      Reader App  ──── Logger App                 │
│                          └──── POSIX Shared Memory (IPC) ───┘   │
├─────────────────────────────────────────────────────────────────┤
│  [ Kernel Space ]   LKM: I2C Character Device Driver            │
│                     file_ops: open / read / write / ioctl       │
│                     kernel memory management (kmalloc/kfree)    │
├─────────────────────────────────────────────────────────────────┤
│  [ Hardware Layer ] ARM64 / AArch64  (QEMU virt simulation)     │
└─────────────────────────────────────────────────────────────────┘
          ▲                                        ▲
  Cross-Compilation                           CI/CD Pipeline
  Docker + musl + gcc                     GitHub Actions (smoke tests)
  binutils (ARM64 target)                 automated QEMU boot verify
```

</details>

<details>
<summary><b>▶ Component Breakdown</b></summary>

<br>

| Layer | Component | Implementation Detail |
|-------|-----------|----------------------|
| **Kernel** | I2C LKM (Character Device) | Custom `file_operations`: `open`, `read`, `write`, `ioctl`; kernel memory via `kmalloc`/`kfree` |
| **IPC** | POSIX Shared Memory | Concurrent reader + logger; mutex-guarded critical sections; data integrity guarantees |
| **Filesystem** | Minimal RootFS | BusyBox-based Linux FHS from scratch; init scripts; device nodes |
| **Build** | Cross-Compilation Pipeline | Docker-containerized ARM64 toolchain: `binutils` + `gcc` + `musl libc` |
| **Emulation** | QEMU ARM64 | Full `virt` machine emulation; automated boot + functional smoke tests |
| **Dashboard** | Web Telemetry UI | BusyBox `httpd` + CGI scripting; real-time data visualization |
| **AI Layer** | Diagnostic Engine | Google Gemini API integration; automated log analysis + anomaly detection |
| **CI/CD** | GitHub Actions | Cross-compilation validation; QEMU boot verification; regression testing |

</details>

---

## `$ ls -la ~/projects/`

### Systems & Concurrent Programming

**[multi-thread-file-sync](https://github.com/livaiyena/multi-thread-file-sync)**
![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![POSIX](https://img.shields.io/badge/POSIX_Threads-FCC624?style=flat-square&logo=linux&logoColor=black)

High-performance file synchronization engine built on POSIX threads. Implements producer-consumer patterns with thread-safe data structures, mutex/semaphore synchronization, and fine-grained memory management. Designed for throughput under concurrent I/O load.

<details>
<summary><b>▶ Technical details</b></summary>

- Thread pool with configurable worker count
- Mutex-protected shared queues (producer-consumer)
- Memory-mapped I/O for large file handling
- Custom arena allocator to minimize `malloc` overhead
- Signal-safe shutdown and cleanup paths

</details>
---

### Data Structures & Algorithms

**[a-maze-ing](https://github.com/livaiyena/a-maze-ing)**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Maze generation and pathfinding via recursive backtracking DFS (generation) and BFS/A* (solving). Demonstrates graph traversal and stack/queue implementation from scratch.

**[push_swap](https://github.com/livaiyena/push_swap)**
![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)

Stack-based sorting with instruction sequence optimization. Achieves sub-linear average-case operation counts through algorithmic analysis of input distributions and greedy pivot selection.

**[get_next_line](https://github.com/livaiyena/get_next_line)**
![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)

Efficient line-by-line file reader with custom static buffer management. Minimizes `read()` syscall frequency and avoids heap fragmentation through careful buffer reuse strategy. Handles arbitrary `BUFFER_SIZE` at compile time.

---

### Foundational Systems Work

**[libft](https://github.com/livaiyena/libft)**
![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)

Ground-up reimplementation of the C standard library: string ops, memory allocators, linked list primitives, and I/O utilities. Serves as the base dependency for all subsequent systems projects. Zero external dependencies.

**[printf](https://github.com/livaiyena/printf)**
![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)

Custom `printf` with format string parser and variadic argument handling. Implements `%d`, `%s`, `%x`, `%p`, `%f` conversion specifiers with correct edge-case behavior (null pointers, INT_MIN, unsigned overflow).

---

<!-- Other Projects -->

---

## `$ cat /etc/tech-stack`

### Languages
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

### Kernel & Embedded
![Linux](https://img.shields.io/badge/Linux_Kernel-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![ARM](https://img.shields.io/badge/ARM64-0091BD?style=for-the-badge&logo=arm&logoColor=white)
![QEMU](https://img.shields.io/badge/QEMU-FF6600?style=for-the-badge&logo=qemu&logoColor=white)
![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)

### Build & DevOps
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![GCC](https://img.shields.io/badge/GCC-A42E2B?style=for-the-badge&logo=gnu&logoColor=white)
![CMake](https://img.shields.io/badge/CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

### Platforms & Protocols
![AWS](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

### Specializations

| Domain | Competencies |
|--------|-------------|
| **Kernel Development** | LKM authoring, character devices, `file_operations`, `ioctl`, interrupt handlers |
| **Embedded Linux** | Cross-compilation pipelines, rootfs construction, BusyBox, init systems |
| **IPC & Concurrency** | POSIX shared memory, semaphores, mutexes, producer-consumer architectures |
| **Memory Management** | Arena allocators, `kmalloc`/`kfree`, buffer strategy, fragmentation avoidance |
| **I/O Systems** | Async I/O, `mmap`, syscall minimization, custom buffering |
| **Networking** | OSPF, BGP, MQTT, TCP/IP stack fundamentals |

---

## `$ cat ~/stats`

<div align="center">

[![GitHub Stats](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=livaiyena&theme=github_dark)](https://github.com/livaiyena)
[![Commit Activity](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=livaiyena&theme=github_dark)](https://github.com/livaiyena)

[![Profile Overview](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=livaiyena&theme=github_dark)](https://github.com/livaiyena)

</div>

---

<div align="center">

*Kernel space to application layer — building systems that work at every level of the stack.*

[![Email](https://img.shields.io/badge/apaydinkerem18%40gmail.com-reach%20out-0a0e17?style=flat-square&logo=gmail&logoColor=00d4ff)](mailto:apaydinkerem18@gmail.com)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d4ff,50:0d2137,100:0a0e17&height=80&section=footer" />

</div>
