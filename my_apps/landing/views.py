from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "./index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["technologies"] = [
            {
                "name": "Python",
                "level": 85,
                "icon": "bi bi-code-slash",
            },
            {
                "name": "Django",
                "level": 80,
                "icon": "bi bi-server",
            },
            {
                "name": "JavaScript",
                "level": 60,
                "icon": "bi bi-filetype-js",
            },
            {
                "name": "SQL",
                "level": 75,
                "icon": "bi bi-database",
            },
            {
                "name": "Linux",
                "level": 55,
                "icon": "bi bi-terminal",
            },
        ]

        # Future database integration:
        # context["projects"] = Project.objects.filter(
        #     is_published=True
        # )[:3]
        #
        # context["posts"] = Post.objects.filter(
        #     is_published=True
        # ).order_by("-created_at")[:3]

        return context
