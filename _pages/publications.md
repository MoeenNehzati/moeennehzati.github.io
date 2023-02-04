---
layout: page
permalink: /publications/
title: publications
description: ""
years: [2020S]
nav: true
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @* %}
{% endfor %}

</div>
