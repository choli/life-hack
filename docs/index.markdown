---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

list all my entries:

{% if site.paginate %}
  {% assign posts = paginator.posts %}
{% else %}
  {% assign posts = site.posts %}
{% endif %}


{%- if posts.size > 0 -%}
  {%- if page.list_title -%}
    ## {{ page.list_title }}
  {%- endif -%}

  {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}

  {%- for post in posts -%}
    - **[{{ post.title | escape }}]({{ post.url | relative_url }})**  
    _{{ post.date | date: date_format }}_

    {%- if site.minima.show_excerpts -%}
      {{ post.excerpt | strip_html | strip_newlines }}
    {%- endif -%}

  {%- endfor -%}

  {%- if site.paginate -%}
    ---
    **Page {{ paginator.page }}**

    {%- if paginator.previous_page -%}
      [← Previous]({{ paginator.previous_page_path | relative_url }})
    {%- else -%}
      •
    {%- endif -%}

    {%- if paginator.next_page -%}
      [Next →]({{ paginator.next_page_path | relative_url }})
    {%- else -%}
      •
    {%- endif -%}
  {%- endif -%}

[Subscribe to our Podcast](https://choli.github.io/life-hack/feed.xml)
{%- endif -%}