import pytest
import tempfile
import os
from wujing.rag.markdown import MarkdownProcessor, create_default_processor


class TestMarkdownProcessor:
    """MarkdownProcessor 类的测试用例"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.processor = MarkdownProcessor()
        self.sample_markdown = """
# 主标题

这是主要内容。

## 子标题

这是子标题下的内容。

### 三级标题

- 列表项1
- 列表项2

```python
def hello():
    print("Hello World!")
```

这是代码块后的内容。
"""

    def test_init_default_parameters(self):
        """测试默认参数初始化"""
        processor = MarkdownProcessor()
        assert processor.parser is not None

    def test_init_custom_parameters(self):
        """测试自定义参数初始化"""
        processor = MarkdownProcessor(include_metadata=False, include_prev_next_rel=False)
        assert processor.parser is not None

    def test_parse_markdown_text(self):
        """测试解析 Markdown 文本"""
        nodes = self.processor.parse_markdown_text(self.sample_markdown)
        
        assert isinstance(nodes, list)
        assert len(nodes) > 0
        
        # 检查节点内容
        for node in nodes:
            assert hasattr(node, 'get_content')
            assert hasattr(node, 'metadata')
            content = node.get_content()
            assert isinstance(content, str)
            assert len(content) > 0

    def test_parse_empty_markdown_text(self):
        """测试解析空 Markdown 文本"""
        nodes = self.processor.parse_markdown_text("")
        assert isinstance(nodes, list)

    def test_parse_markdown_file(self):
        """测试解析 Markdown 文件"""
        # 创建临时 Markdown 文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write(self.sample_markdown)
            temp_file_path = f.name

        try:
            nodes = self.processor.parse_markdown_file(temp_file_path)
            
            assert isinstance(nodes, list)
            assert len(nodes) > 0
            
            # 验证内容与直接解析文本的结果一致
            text_nodes = self.processor.parse_markdown_text(self.sample_markdown)
            assert len(nodes) == len(text_nodes)
            
        finally:
            # 清理临时文件
            os.unlink(temp_file_path)

    def test_parse_nonexistent_file(self):
        """测试解析不存在的文件"""
        with pytest.raises(FileNotFoundError):
            self.processor.parse_markdown_file("/nonexistent/path/file.md")

    def test_get_node_summaries(self):
        """测试获取节点摘要"""
        nodes = self.processor.parse_markdown_text(self.sample_markdown)
        summaries = self.processor.get_node_summaries(nodes)
        
        assert isinstance(summaries, list)
        assert len(summaries) == len(nodes)
        
        for i, summary in enumerate(summaries):
            assert isinstance(summary, dict)
            assert 'index' in summary
            assert 'content_preview' in summary
            assert 'content_length' in summary
            assert 'metadata' in summary
            assert summary['index'] == i + 1
            assert isinstance(summary['content_length'], int)
            assert summary['content_length'] >= 0

    def test_get_node_summaries_with_max_length(self):
        """测试带长度限制的节点摘要"""
        nodes = self.processor.parse_markdown_text(self.sample_markdown)
        max_length = 50
        summaries = self.processor.get_node_summaries(nodes, max_content_length=max_length)
        
        for summary in summaries:
            if summary['content_length'] > max_length:
                # 如果原内容长度超过限制，预览应该以"..."结尾
                assert summary['content_preview'].endswith("...")
                # 预览长度应该是 max_length + 3 (for "...")
                assert len(summary['content_preview']) == max_length + 3
            else:
                # 如果原内容长度不超过限制，预览应该等于原内容
                assert not summary['content_preview'].endswith("...")

    def test_print_node_summaries(self, capsys):
        """测试打印节点摘要"""
        nodes = self.processor.parse_markdown_text(self.sample_markdown)
        self.processor.print_node_summaries(nodes, max_content_length=50)
        
        captured = capsys.readouterr()
        assert "--- NODE" in captured.out
        assert "Text:" in captured.out
        assert "Content Length:" in captured.out
        assert "Metadata:" in captured.out

    def test_extract_document_title(self):
        """测试提取文档标题"""
        # 测试有标题的情况
        markdown_with_title = "# 这是文档标题\n\n这是内容。"
        title = self.processor._extract_document_title(markdown_with_title)
        assert title == "这是文档标题"
        
        # 测试没有标题的情况
        markdown_without_title = "这是没有标题的内容。\n\n## 这是二级标题"
        title = self.processor._extract_document_title(markdown_without_title)
        assert title is None
        
        # 测试空字符串
        title = self.processor._extract_document_title("")
        assert title is None
        
        # 测试只有 # 符号的情况
        markdown_empty_title = "# \n\n内容"
        title = self.processor._extract_document_title(markdown_empty_title)
        assert title is None
        
        # 测试多个一级标题的情况（应该返回第一个）
        markdown_multiple_titles = "# 第一个标题\n\n内容\n\n# 第二个标题\n\n更多内容"
        title = self.processor._extract_document_title(markdown_multiple_titles)
        assert title == "第一个标题"
        
        # 测试文档开头有其他内容，但后面有一级标题的情况
        markdown_title_not_first = """
这是前言内容。
更多前言。

# 实际的主标题

这是正文内容。

# 第二个标题

更多内容。
"""
        title = self.processor._extract_document_title(markdown_title_not_first)
        assert title == "实际的主标题"  # 应该选择第一个一级标题
        
        # 测试文档开头就有一级标题的情况（优先级更高）
        markdown_title_at_beginning = """# 开头的标题

一些内容。

# 后面的标题

更多内容。
"""
        title = self.processor._extract_document_title(markdown_title_at_beginning)
        assert title == "开头的标题"

    def test_extract_title_excludes_code_blocks(self):
        """测试标题提取时排除代码块中的内容"""
        markdown_with_code = """
# 真正的标题

这是正常内容。

```python
# 这不是真正的标题
def function():
    # 这也不是标题
    pass
```

## 这是二级标题

```bash
# 这也不是标题，是 bash 注释
echo "hello"
```

# 第二个真正的标题

结束内容。
"""
        
        title = self.processor._extract_document_title(markdown_with_code)
        assert title == "真正的标题"
        
        all_titles = self.processor._extract_all_document_titles(markdown_with_code)
        assert all_titles == ["真正的标题", "第二个真正的标题"]

    def test_extract_all_document_titles(self):
        """测试提取所有文档标题"""
        # 测试多个一级标题
        markdown_multiple = """
# 第一章 介绍

内容1

## 1.1 子节

内容

# 第二章 方法

内容2

# 第三章 结论

内容3
"""
        all_titles = self.processor._extract_all_document_titles(markdown_multiple)
        expected = ["第一章 介绍", "第二章 方法", "第三章 结论"]
        assert all_titles == expected
        
        # 测试没有一级标题
        markdown_no_h1 = "## 只有二级标题\n\n内容"
        all_titles = self.processor._extract_all_document_titles(markdown_no_h1)
        assert all_titles == []
        
        # 测试单个一级标题
        markdown_single = "# 单个标题\n\n内容"
        all_titles = self.processor._extract_all_document_titles(markdown_single)
        assert all_titles == ["单个标题"]

    def test_document_title_in_metadata(self):
        """测试文档标题是否正确添加到节点的 metadata 中"""
        markdown_with_title = """
# 测试文档标题

这是第一段内容。

## 子标题

这是子标题下的内容。
"""
        
        nodes = self.processor.parse_markdown_text(markdown_with_title)
        
        # 检查所有节点都包含文档标题信息
        for node in nodes:
            assert hasattr(node, 'metadata')
            assert node.metadata is not None
            assert 'document_title' in node.metadata
            assert node.metadata['document_title'] == "测试文档标题"
            assert 'all_h1_titles' in node.metadata
            assert node.metadata['all_h1_titles'] == ["测试文档标题"]
            assert 'h1_count' in node.metadata
            assert node.metadata['h1_count'] == 1

    def test_multiple_h1_titles_in_metadata(self):
        """测试多个一级标题的处理"""
        markdown_multiple_h1 = """
# 第一章 介绍

这是介绍部分的内容。

## 1.1 背景

背景信息。

# 第二章 方法

这是方法部分的内容。

# 第三章 结论

结论内容。
"""
        
        nodes = self.processor.parse_markdown_text(markdown_multiple_h1)
        
        expected_titles = ["第一章 介绍", "第二章 方法", "第三章 结论"]
        
        # 检查所有节点都包含完整的标题信息
        for node in nodes:
            assert hasattr(node, 'metadata')
            assert node.metadata is not None
            # 主标题应该是第一个
            assert 'document_title' in node.metadata
            assert node.metadata['document_title'] == "第一章 介绍"
            # 所有一级标题
            assert 'all_h1_titles' in node.metadata
            assert node.metadata['all_h1_titles'] == expected_titles
            # 标题数量
            assert 'h1_count' in node.metadata
            assert node.metadata['h1_count'] == 3

    def test_document_title_with_disabled_metadata(self):
        """测试禁用元数据时不添加文档标题"""
        processor_no_metadata = MarkdownProcessor(include_metadata=False)
        markdown_with_title = "# 测试标题\n\n内容"
        
        nodes = processor_no_metadata.parse_markdown_text(markdown_with_title)
        
        # 当 include_metadata=False 时，不应该添加文档标题
        for node in nodes:
            if hasattr(node, 'metadata') and node.metadata:
                assert 'document_title' not in node.metadata

    def test_document_title_with_chunking(self):
        """测试带分块功能的处理器中文档标题的传递"""
        # 创建一个会触发分块的长文档
        long_content = "这是一段很长的内容。" * 50  # 创建长内容以触发分块
        markdown_with_title = f"""# 长文档标题

{long_content}

## 子标题

{long_content}

# 第二章标题

更多内容。
"""
        
        processor_with_chunking = MarkdownProcessor(
            include_metadata=True,
            chunk_size=100,  # 设置较小的分块大小以确保会分块
            chunk_overlap=20
        )
        
        nodes = processor_with_chunking.parse_markdown_text(markdown_with_title)
        
        # 所有节点都应该包含完整的文档标题信息
        expected_all_titles = ["长文档标题", "第二章标题"]
        
        for node in nodes:
            assert hasattr(node, 'metadata')
            assert node.metadata is not None
            # 主标题
            assert 'document_title' in node.metadata
            assert node.metadata['document_title'] == "长文档标题"
            # 所有标题
            assert 'all_h1_titles' in node.metadata
            assert node.metadata['all_h1_titles'] == expected_all_titles
            # 标题计数
            assert 'h1_count' in node.metadata
            assert node.metadata['h1_count'] == 2


class TestCreateDefaultProcessor:
    """测试默认处理器创建函数"""

    def test_create_default_processor(self):
        """测试创建默认处理器"""
        processor = create_default_processor()
        
        assert isinstance(processor, MarkdownProcessor)
        assert processor.parser is not None


class TestMarkdownProcessorIntegration:
    """MarkdownProcessor 集成测试"""

    def test_full_workflow(self):
        """测试完整工作流程"""
        markdown_content = """
# 测试文档

这是一个测试文档。

## 第一章

第一章的内容。

### 1.1 小节

小节内容。

## 第二章

第二章的内容。

```python
print("Hello World!")
```

结束。
"""
        
        # 创建处理器
        processor = create_default_processor()
        
        # 解析内容
        nodes = processor.parse_markdown_text(markdown_content)
        
        # 获取摘要
        summaries = processor.get_node_summaries(nodes)
        
        # 验证结果
        assert len(nodes) > 0
        assert len(summaries) == len(nodes)
        assert all(summary['content_length'] > 0 for summary in summaries)
        
        # 验证包含标题信息
        content_texts = [node.get_content() for node in nodes]
        full_content = "\n".join(content_texts)
        assert "测试文档" in full_content or any("测试文档" in text for text in content_texts)

    def test_chinese_content_handling(self):
        """测试中文内容处理"""
        chinese_markdown = """
# 中文标题

这是中文内容，包含一些特殊字符：你好世界！

## 子标题

- 第一项
- 第二项
- 第三项

### 代码示例

```python
# 中文注释
def 问候(名字):
    print(f"你好，{名字}！")
```

这是结束部分。
"""
        
        processor = create_default_processor()
        nodes = processor.parse_markdown_text(chinese_markdown)
        summaries = processor.get_node_summaries(nodes)
        
        assert len(nodes) > 0
        assert len(summaries) == len(nodes)
        
        # 验证中文内容正确处理
        for summary in summaries:
            assert summary['content_length'] > 0
            assert isinstance(summary['content_preview'], str)
        
        # 验证中文标题正确提取并添加到 metadata
        for node in nodes:
            assert hasattr(node, 'metadata')
            assert node.metadata is not None
            assert 'document_title' in node.metadata
            assert node.metadata['document_title'] == "中文标题"

    def test_document_title_extraction_edge_cases(self):
        """测试文档标题提取的边缘情况"""
        processor = create_default_processor()
        
        # 测试标题前有其他内容的情况
        markdown1 = """
这是前言内容。

# 实际标题

这是正文内容。
"""
        nodes1 = processor.parse_markdown_text(markdown1)
        for node in nodes1:
            if hasattr(node, 'metadata') and node.metadata:
                assert node.metadata.get('document_title') == "实际标题"
        
        # 测试没有一级标题，只有二级标题的情况
        markdown2 = """
## 二级标题

这是内容。

### 三级标题

更多内容。
"""
        nodes2 = processor.parse_markdown_text(markdown2)
        for node in nodes2:
            if hasattr(node, 'metadata') and node.metadata:
                assert 'document_title' not in node.metadata or node.metadata['document_title'] is None


if __name__ == "__main__":
    pytest.main([__file__])