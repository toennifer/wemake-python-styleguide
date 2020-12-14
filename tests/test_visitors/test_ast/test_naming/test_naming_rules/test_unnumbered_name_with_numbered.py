import pytest

from wemake_python_styleguide.violations.naming import (
    UnNumberedNameWithNumberedNameViolation,
)
from wemake_python_styleguide.visitors.ast.naming import UnNumberedNameWithNumberedNameVisitor


@pytest.mark.parametrize('unnumbered_name_with_numbered', [
    'x',
    'x2',
])
def test_wrong_numbered_name(
    assert_errors,
    assert_error_text,
    parse_ast_tree,
    naming_template,
    default_options,
    mode,
    unnumbered_name_with_numbered,
):
    """Ensures that unnumbered names with numbered names are not allowed."""
    tree = parse_ast_tree(mode(naming_template.format(
    unnumbered_name_with_numbered)))

    visitor = UnNumberedNameWithNumberedNameVisitor(default_options, tree=tree)
    visitor.run()

    assert_errors(visitor, [UnNumberedNameWithNumberedNameViolation])
    assert_error_text(visitor, unnumbered_name_with_numbered)


@pytest.mark.parametrize('numbered_name', [
    'x1',
    'x2',
])
def test_correct_numbered_name(
    assert_errors,
    parse_ast_tree,
    naming_template,
    default_options,
    mode,
    numbered_name,
):
    """Ensures that unnumbered names with numbered names are not allowed."""
    tree = parse_ast_tree(mode(naming_template.format(numbered_name)))

    visitor = UnNumberedNameWithNumberedNameVisitor(default_options, tree=tree)
    visitor.run()

    assert_errors(visitor, [])


@pytest.mark.parametrize('unnumbered_name', [
    'x',
])
def test_correct_unnumbered_name(
    assert_errors,
    parse_ast_tree,
    naming_template,
    default_options,
    mode,
    unnumbered_name,
):
    """Ensures that unnumbered names with numbered names are not allowed."""
    tree = parse_ast_tree(mode(naming_template.format(unnumbered_name)))

    visitor = UnNumberedNameWithNumberedNameVisitor(default_options, tree=tree)
    visitor.run()

    assert_errors(visitor, [])
