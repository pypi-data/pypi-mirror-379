"""Template management for ansible-docsmith."""

import shutil
import tempfile
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError, select_autoescape


class TemplateManager:
    """Manage templates for documentation generation."""

    def __init__(
        self, template_dir: Path | None = None, template_file: Path | None = None
    ):
        """Initialize template manager.

        Args:
            template_dir: Custom template directory. If None, uses built-in templates.
            template_file: Single template file. If provided, creates temporary
                directory structure.
        """
        self._temp_dir = None

        if template_file:
            self.template_dir = self._setup_single_template_file(template_file)
        else:
            self.template_dir = template_dir or self._get_builtin_template_dir()

        self.env = self._setup_jinja_env()

    def _get_builtin_template_dir(self) -> Path:
        """Get the built-in template directory."""
        return Path(__file__).parent

    def _setup_single_template_file(self, template_file: Path) -> Path:
        """Set up temporary directory structure for single template file.

        Args:
            template_file: Path to the single template file

        Returns:
            Path to temporary directory containing the template structure

        Raises:
            ValueError: If template file has invalid syntax
        """
        # Validate template syntax first
        self._validate_template_syntax(template_file)

        # Create temporary directory
        self._temp_dir = Path(tempfile.mkdtemp(prefix="ansible_docsmith_template_"))

        # Always use readme subdirectory (template type)
        readme_dir = self._temp_dir / "readme"
        readme_dir.mkdir()

        # Determine template extension based on file extension
        if template_file.suffix in [".rst", ".txt"]:
            template_dest = readme_dir / "default.rst.j2"
        else:
            template_dest = readme_dir / "default.md.j2"
        shutil.copy2(template_file, template_dest)

        return self._temp_dir

    def _validate_template_syntax(self, template_file: Path):
        """Validate Jinja2 template syntax.

        Args:
            template_file: Path to template file to validate

        Raises:
            ValueError: If template has invalid syntax
        """
        try:
            content = template_file.read_text(encoding="utf-8")
            # Create a temporary environment to parse the template
            temp_env = Environment()
            temp_env.parse(content)
        except TemplateSyntaxError as e:
            raise ValueError(f"Invalid template syntax in {template_file}: {e}")
        except Exception as e:
            raise ValueError(f"Error reading template file {template_file}: {e}")

    def cleanup(self):
        """Clean up temporary directories if they exist."""
        if self._temp_dir and self._temp_dir.exists():
            shutil.rmtree(self._temp_dir)
            self._temp_dir = None

    def __del__(self):
        """Clean up temporary directories on deletion."""
        self.cleanup()

    def _setup_jinja_env(self) -> Environment:
        """Setup Jinja2 environment with proper loader."""
        return Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def add_filter(self, name: str, filter_func) -> None:
        """Add custom filter to the Jinja environment."""
        self.env.filters[name] = filter_func

    def get_template(
        self,
        template_name: str,
        template_type: str = "readme",
        format_type: str = "markdown",
    ) -> str:
        """Get template content by name, type and format.

        Args:
            template_name: Name of the template (e.g., 'default')
            template_type: Type of template (e.g., 'readme')
            format_type: Output format ('markdown' or 'rst')

        Returns:
            Template content as string
        """
        # Determine file extension based on format
        ext = "rst.j2" if format_type.lower() == "rst" else "md.j2"
        template_path = f"{template_type}/{template_name}.{ext}"
        # Read template file directly to get source content
        template_file = self.template_dir / template_path
        return template_file.read_text(encoding="utf-8")

    def render_template(
        self,
        template_name: str,
        template_type: str = "readme",
        format_type: str = "markdown",
        **context,
    ) -> str:
        """Render template with given context.

        Args:
            template_name: Name of the template (e.g., 'default')
            template_type: Type of template (e.g., 'readme')
            format_type: Output format ('markdown' or 'rst')
            **context: Template context variables

        Returns:
            Rendered template content
        """
        # Determine file extension based on format
        ext = "rst.j2" if format_type.lower() == "rst" else "md.j2"
        template_path = f"{template_type}/{template_name}.{ext}"
        template = self.env.get_template(template_path)
        return template.render(**context)

    def list_templates(self, template_type: str = "readme") -> list[str]:
        """List available templates of given type.

        Args:
            template_type: Type of template to list

        Returns:
            List of available template names (without extension)
        """
        template_dir = self.template_dir / template_type
        if not template_dir.exists():
            return []

        templates = []
        for template_file in template_dir.glob("*.j2"):
            # Remove extension to get template name
            name = template_file.stem
            # Remove format-specific suffix (.md or .rst)
            if name.endswith(".md") or name.endswith(".rst"):
                name = name[:-4] if name.endswith(".rst") else name[:-3]
            templates.append(name)

        return sorted(templates)


__all__ = ["TemplateManager"]
