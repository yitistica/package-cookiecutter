.. comment:
   --------------
   Section: Setting
   --------------

{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

.. comment:
   --------------
   Section: Title
   --------------

{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

.. comment:
   --------------
   Section: Badges
      - testing workflow: pre-release-test.yml
   --------------

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.pypi_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.pypi_slug }}

..  image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/pre-release-test.yml/badge.svg
        :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/pre-release-test.yml

.. image:: https://readthedocs.org/projects/{{ cookiecutter.readthedocs_slug }}/badge/?version=latest
        :target: https://{{ cookiecutter.readthedocs_slug }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}


{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.readthedocs_slug }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------

This package was created with the `yitistica/package-cookiecutter`_ project template using Cookiecutter_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _yitistica/package-cookiecutter: https://github.com/yitistica/package-cookiecutter
