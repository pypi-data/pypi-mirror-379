from django.contrib import messages
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class MessageViewMixin:
    def message_user(self, message, level=None, extra_tags=None, fail_silently=None):
        """
        Send a message to the user. The default implementation
        posts a message using the django.contrib.messages backend.

        Exposes almost the same API as messages.add_message(), but accepts the
        positional arguments in a different order to maintain backwards
        compatibility. For convenience, it accepts the `level` argument as
        a string rather than the usual level number.
        """
        level = level or messages.ERROR
        extra_tags = extra_tags or ""
        if not isinstance(level, int):
            # attempt to get the level if passed a string
            try:
                level = getattr(messages.constants, level.upper())
            except AttributeError:
                levels = ", ".join(
                    [level for level in messages.constants.DEFAULT_TAGS.values()]
                )
                raise ValueError(
                    f"Bad message level string: `{level}`. Possible values are: {levels}"
                )

        messages.add_message(
            self.request,
            level,
            format_html("{}", mark_safe(message)),  # nosec B703 B308
            extra_tags=extra_tags,
            fail_silently=fail_silently,
        )
