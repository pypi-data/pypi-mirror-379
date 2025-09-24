#!/usr/bin/env python3
"""
每日提交代码行数统计脚本
该脚本用于统计Git仓库中master分支每天提交的代码行数，包括新增行数、删除行数和净变化行数

使用方法:
1. 作为命令行工具：
   pixelarraylib summary_code_count --since="2025-05-09"
   pixelarraylib summary_code_count --author="张三"
   pixelarraylib summary_code_count --output=stats.csv
   pixelarraylib summary_code_count --file-types="py,js,vue"

2. 作为Python模块：
   from pixelarraylib.scripts.summary_code_count import main
   main()
"""

import os
import subprocess
import argparse
from datetime import datetime, timedelta
from collections import defaultdict
import pandas as pd


class GitCommitStatsAnalyzer:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path
        self.daily_stats = defaultdict(
            lambda: {
                "commits": 0,
                "added_lines": 0,
                "deleted_lines": 0,
                "net_lines": 0,
                "authors": set(),
                "files_changed": 0,
            }
        )

    def is_git_repo(self):
        """检查是否为git仓库"""
        return os.path.exists(os.path.join(self.repo_path, ".git"))

    def run_git_command(self, command):
        """执行git命令并返回结果"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            # 对于某些预期的错误（如第一个提交），不打印错误信息
            if "unknown revision" in e.stderr or "ambiguous argument" in e.stderr:
                return ""
            else:
                print(f"Git命令执行失败: {command}")
                print(f"错误信息: {e.stderr}")
            return ""

    def get_commit_list(self, since_date=None, until_date=None, author=None):
        """获取master分支的提交列表"""
        command = 'git log master --oneline --pretty=format:"%H|%ad|%an" --date=short'

        if since_date:
            command += f' --since="{since_date}"'
        if until_date:
            command += f' --until="{until_date}"'
        if author:
            command += f' --author="{author}"'

        output = self.run_git_command(command)
        commits = []

        for line in output.split("\n"):
            if line:
                parts = line.split("|")
                if len(parts) >= 3:
                    commit_hash = parts[0]
                    commit_date = parts[1]
                    commit_author = parts[2]
                    commits.append(
                        {
                            "hash": commit_hash,
                            "date": commit_date,
                            "author": commit_author,
                        }
                    )

        return commits

    def get_commit_stats(self, commit_hash, file_types=None):
        """获取单个提交的统计信息"""
        # 首先检查是否有父提交
        parent_check = self.run_git_command(f"git rev-parse {commit_hash}^ 2>/dev/null || echo 'NO_PARENT'")
        
        if parent_check.strip() == "NO_PARENT":
            # 这是第一个提交，没有父提交，使用空树作为比较基准
            command = f"git diff --numstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 {commit_hash}"
        else:
            # 有父提交，正常比较
            command = f"git diff --numstat {commit_hash}^..{commit_hash}"
        
        output = self.run_git_command(command)

        added_lines = 0
        deleted_lines = 0
        files_changed = 0

        for line in output.split("\n"):
            if line:
                parts = line.split("\t")
                if len(parts) >= 3:
                    try:
                        added = int(parts[0]) if parts[0] != "-" else 0
                        deleted = int(parts[1]) if parts[1] != "-" else 0
                        filename = parts[2]

                        # 如果指定了文件类型过滤
                        if file_types:
                            file_ext = filename.split(".")[-1].lower()
                            if file_ext not in file_types:
                                continue

                        added_lines += added
                        deleted_lines += deleted
                        files_changed += 1
                    except (ValueError, IndexError):
                        continue

        return {
            "added_lines": added_lines,
            "deleted_lines": deleted_lines,
            "net_lines": added_lines - deleted_lines,
            "files_changed": files_changed,
        }

    def analyze_commits(
        self, since_date=None, until_date=None, author=None, file_types=None
    ):
        """分析master分支的提交统计"""
        if not self.is_git_repo():
            print("错误：当前目录不是Git仓库")
            return False

        print("正在分析Git master分支的提交历史...")
        commits = self.get_commit_list(since_date, until_date, author)

        if not commits:
            print("没有找到符合条件的提交")
            return False

        total_commits = len(commits)
        print(f"找到 {total_commits} 个提交，正在统计...")

        for i, commit in enumerate(commits):
            # 显示进度
            if i % 10 == 0 or i == total_commits - 1:
                progress = (i + 1) / total_commits * 100
                print(f"进度: {progress:.1f}% ({i + 1}/{total_commits})")

            commit_date = commit["date"]
            commit_author = commit["author"]

            stats = self.get_commit_stats(commit["hash"], file_types)

            # 累加到日统计
            day_stats = self.daily_stats[commit_date]
            day_stats["commits"] += 1
            day_stats["added_lines"] += stats["added_lines"]
            day_stats["deleted_lines"] += stats["deleted_lines"]
            day_stats["net_lines"] += stats["net_lines"]
            day_stats["authors"].add(commit_author)
            day_stats["files_changed"] += stats["files_changed"]

        print("分析完成！")
        return True

    def print_stats(self):
        """使用pandas DataFrame打印统计结果"""
        if not self.daily_stats:
            print("没有统计数据")
            return

        # 准备DataFrame数据
        data = []
        all_authors = set()

        # 按日期排序
        sorted_dates = sorted(self.daily_stats.keys())

        for date in sorted_dates:
            stats = self.daily_stats[date]
            all_authors.update(stats["authors"])

            data.append(
                {
                    "Date": date,
                    "Commits": stats["commits"],
                    "Added": stats["added_lines"],
                    "Deleted": stats["deleted_lines"],
                    "Net": stats["net_lines"],  # 保持为数字类型
                    "Authors": len(stats["authors"]),
                    "Files": stats["files_changed"],
                    "Author List": ", ".join(sorted(stats["authors"])),
                }
            )

        # 创建DataFrame
        df = pd.DataFrame(data)

        if df.empty:
            print("没有统计数据")
            return

        # 设置pandas显示选项
        pd.set_option("display.max_columns", None)
        pd.set_option("display.width", None)
        pd.set_option("display.max_colwidth", 50)

        # 定义每列的宽度（调整为更合适的宽度）
        column_widths = {
            "Date": 15,  # 增加宽度，确保日期完整显示
            "Commits": 12,  # 增加宽度，考虑标题长度
            "Added": 12,  # 增加宽度，考虑大数字
            "Deleted": 12,  # 增加宽度，考虑大数字
            "Net": 12,  # 增加宽度，考虑符号和大数字
            "Authors": 10,  # 增加宽度，考虑标题长度
            "Files": 10,  # 增加宽度，考虑标题长度
        }

        # 打印主表格（不包含作者列表）
        display_df = df.drop("Author List", axis=1).copy()

        # 格式化净变化列，添加正负号
        display_df["Net"] = display_df["Net"].apply(
            lambda x: f"+{x}" if x > 0 else str(x)
        )

        # 计算总宽度（包括列之间的空格）
        total_width = sum(column_widths.values()) + len(column_widths) - 1

        # 打印表头
        print("\n" + "=" * total_width)
        print(f"{'每日代码提交统计 (master分支)':^{total_width}}")  # 居中显示标题
        print("=" * total_width)

        # 打印列标题
        header = ""
        for col, width in column_widths.items():
            header += f"{col:^{width}} "  # 使用^实现居中对齐
        print(header.rstrip())
        print("-" * total_width)

        # 打印数据行
        for _, row in display_df.iterrows():
            line = ""
            for col, width in column_widths.items():
                value = str(row[col])  # 转换为字符串
                if col == "Date":
                    # 日期左对齐
                    line += f"{value:<{width}} "
                elif col == "Net":
                    # 净变化右对齐，确保符号对齐
                    line += f"{value:>{width}} "
                else:
                    # 其他数字右对齐
                    line += f"{value:>{width}} "
            print(line.rstrip())

        # 计算总计
        total_commits = df["Commits"].sum()
        total_added = df["Added"].sum()
        total_deleted = df["Deleted"].sum()
        total_net = df["Net"].sum()
        total_authors = len(all_authors)
        total_files = df["Files"].sum()

        # 打印总计行
        print("-" * total_width)
        total_net_str = f"+{total_net}" if total_net > 0 else str(total_net)
        total_line = (
            f"{'总计':<{column_widths['Date']}} "
            f"{total_commits:>{column_widths['Commits']}} "
            f"{total_added:>{column_widths['Added']}} "
            f"{total_deleted:>{column_widths['Deleted']}} "
            f"{total_net_str:>{column_widths['Net']}} "
            f"{total_authors:>{column_widths['Authors']}} "
            f"{total_files:>{column_widths['Files']}}"
        )
        print(total_line)

        # 统计摘要
        print("\n📊 统计摘要 (master分支):")
        print(f"  📅 统计天数: {len(df)} 天")
        print(f"  🔄 总提交数: {total_commits:,}")
        print(f"  ➕ 总新增行数: {total_added:,}")
        print(f"  ➖ 总删除行数: {total_deleted:,}")
        print(f"  📈 净变化行数: {total_net:+,}")
        print(f"  👥 参与作者数: {total_authors}")

        if len(df) > 0:
            print(f"  📊 平均每天提交: {total_commits/len(df):.1f}")
            print(f"  📈 平均每天净增: {total_net/len(df):+.1f} 行")

        # 显示TOP统计
        if len(df) > 1:
            print("\n🏆 TOP统计 (master分支):")
            # 最活跃的一天
            max_commits_day = df.loc[df["Commits"].idxmax()]
            print(
                f"  🥇 最多提交日: {max_commits_day['Date']} ({max_commits_day['Commits']} 次提交)"
            )

            # 代码变化最大的一天
            max_lines_day = df.loc[df["Added"].idxmax()]
            print(
                f"  📝 最多新增日: {max_lines_day['Date']} (+{max_lines_day['Added']} 行)"
            )

            # 净增长最大的一天（使用原始数值）
            max_net_day = df.loc[df["Net"].idxmax()]
            net_change_str = (
                f"+{max_net_day['Net']}"
                if max_net_day["Net"] > 0
                else str(max_net_day["Net"])
            )
            print(f"  🚀 最大净增日: {max_net_day['Date']} ({net_change_str} 行)")

        if all_authors:
            print(f"\n👥 参与作者 (master分支): {', '.join(sorted(all_authors))}")

        # 如果数据量不大，显示详细的作者分布
        if len(df) <= 10:
            print(f"\n📋 详细作者分布 (master分支):")
            for _, row in df.iterrows():
                if row["Author List"]:
                    print(f"  {row['Date']}: {row['Author List']}")

    def get_dataframe(self):
        """返回pandas DataFrame格式的统计数据"""
        if not self.daily_stats:
            return pd.DataFrame()

        data = []
        sorted_dates = sorted(self.daily_stats.keys())

        for date in sorted_dates:
            stats = self.daily_stats[date]
            data.append(
                {
                    "日期": date,
                    "提交数": stats["commits"],
                    "新增行数": stats["added_lines"],
                    "删除行数": stats["deleted_lines"],
                    "净变化": stats["net_lines"],
                    "作者数": len(stats["authors"]),
                    "文件数": stats["files_changed"],
                    "作者列表": ", ".join(sorted(stats["authors"])),
                }
            )

        return pd.DataFrame(data)

    def export_to_csv(self, filename):
        """导出统计结果到CSV文件"""
        df = self.get_dataframe()
        if df.empty:
            print("没有统计数据可导出")
            return

        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"📁 统计结果已导出到: {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Git每日代码提交统计工具 (仅统计master分支)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument("--since", "-s", help="开始日期 (格式: YYYY-MM-DD，默认30天前)")
    parser.add_argument("--until", "-u", help="结束日期 (格式: YYYY-MM-DD，默认今天)")
    parser.add_argument("--author", "-a", help="指定作者名称")
    parser.add_argument("--output", "-o", help="输出CSV文件名")
    parser.add_argument(
        "--file-types", "-t", help="指定文件类型，用逗号分隔 (如: py,js,vue)"
    )
    parser.add_argument(
        "--repo-path", "-p", default=".", help="Git仓库路径 (默认当前目录)"
    )

    args = parser.parse_args()

    # 设置默认日期范围（最近30天）
    if not args.since:
        args.since = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

    # 处理文件类型过滤
    file_types = None
    if args.file_types:
        file_types = [ft.strip().lower() for ft in args.file_types.split(",")]

    # 创建分析器实例
    analyzer = GitCommitStatsAnalyzer(args.repo_path)

    # 执行分析
    success = analyzer.analyze_commits(
        since_date=args.since,
        until_date=args.until,
        author=args.author,
        file_types=file_types,
    )

    if success:
        # 显示统计结果
        analyzer.print_stats()

        # 导出CSV（如果指定）
        if args.output:
            analyzer.export_to_csv(args.output)


if __name__ == "__main__":
    main()
