from django.db import models


class Profile(models.Model):
    """Singleton-style model for personal profile info."""
    name = models.CharField(max_length=100, default="Omm Prakash Rout")
    title = models.CharField(max_length=200, default="Software Engineer & Developer")
    # Comma-separated roles for the typewriter effect
    typewriter_roles = models.CharField(
        max_length=500,
        default="Full Stack Developer,Python Enthusiast,Cloud Architect,Software Engineer",
        help_text="Comma-separated roles for the typewriter animation"
    )
    bio_short = models.TextField(
        default="I create beautiful, functional, and user-centered digital experiences. "
                "With a strong passion for web development, I bring ideas to life through "
                "clean code and thoughtful design."
    )
    bio_long = models.TextField(
        default="I'm a creative thinker and developer passionate about building modern, "
                "responsive web applications. My journey began with a love for problem-solving "
                "and evolved into a deep curiosity for how the web works — combining logic with "
                "creativity to bring ideas to life."
    )
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    availability_text = models.CharField(max_length=100, default="Available for freelance work")

    # About section stats
    languages = models.CharField(max_length=200, default="JS, Python, Java, SQL")
    education = models.CharField(max_length=200, default="Computer Science")
    projects_count = models.CharField(max_length=50, default="15+ Built Projects")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

    def get_typewriter_roles(self):
        """Return list of roles for typewriter animation."""
        return [role.strip() for role in self.typewriter_roles.split(',')]


class Skill(models.Model):
    """Individual skill/technology for the tech stack grid."""
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('framework', 'Framework'),
        ('database', 'Database'),
        ('tool', 'Tool / Platform'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    icon_class = models.CharField(
        max_length=100,
        help_text="Phosphor icon class, e.g. 'ph ph-database'"
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    """Portfolio project card."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(
        max_length=300,
        help_text="Comma-separated tags, e.g. 'Python, Django, REST API'"
    )
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_tags_list(self):
        """Return tags as a list."""
        return [tag.strip() for tag in self.tags.split(',')]


class SocialLink(models.Model):
    """Social media links."""
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter/X'),
        ('youtube', 'YouTube'),
        ('other', 'Other'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(
        max_length=100,
        help_text="Phosphor icon class, e.g. 'ph ph-github-logo'"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_platform_display()} — {self.url}"


class ContactInfo(models.Model):
    """Contact details displayed on the contact section."""
    email = models.EmailField(default="ommprakashrout@example.com")
    phone = models.CharField(max_length=30, default="+91 98765 43210")
    location = models.CharField(max_length=200, default="Bhubaneswar, India")
    contact_tagline = models.TextField(
        default="I'm always open to discussing exciting projects and new opportunities. Let's collaborate!"
    )

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.email
