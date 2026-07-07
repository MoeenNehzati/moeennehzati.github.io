---
layout: page
permalink: /research/
title: Research
description: ""
nav: true
---
<!-- _pages/publications.md -->
<div class="publications">

<h2>Work in Progress</h2>
{% bibliography -f papers --group_by none -q @article[status=work-in-progress]* %}

<h2>Published and Preprints</h2>
{% bibliography -f papers -q @article[status!=work-in-progress]* %}
</div>
