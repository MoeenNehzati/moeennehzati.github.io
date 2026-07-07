---
layout: page
title: Projects
permalink: /projects/
description: Selected Technical Projects
nav: true
nav_order: 2
display_categories: [research]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
  {% bibliography -f papers --group_by none -q @software* -T software %}
</div>
