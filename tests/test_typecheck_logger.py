"""Unit tests for type_dict library."""

from contextlib import nullcontext as does_not_raise

from df_typecheck.type_dict import TypeCheckError, TypeCheckLogger
import pytest

# If warning_mode, raise error
# If not warning_mode, return None


@pytest.mark.parametrize(
    'warning_mode,expectation',
    [
        (True, does_not_raise()),
        (False, pytest.raises(TypeCheckError)),
    ],
)
def test_warning_mode(warning_mode, expectation):
    """Test that failed typechecks don't raise an error when in warning mode."""
    typecheck_logger = TypeCheckLogger(warning_mode=warning_mode)

    with expectation:
        typecheck_logger.log_failed_typecheck(
            {'a': str},
            {
                'c': {
                    'type_in_df': str,
                    'correct_type': int,
                },
            },
        )
