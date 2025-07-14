---
layout: page
permalink: /research/
title: Research
description: ""
years: [2040]
nav: true
---
<!-- _pages/publications.md -->
<div class="publications">

<!-- {%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  
{% endfor %} -->
{% bibliography -f papers -q @* %}
</div>
