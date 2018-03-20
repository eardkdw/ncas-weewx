This is (approximately) the WeeWX skin used for the National Centre for Atmospheric Sciences' Davis Vantage weather stations, e.g.

- https://sci.ncas.ac.uk/leedsweather/ (at Leeds University)
- https://sci.ncas.ac.uk/ness/ (at NESS Botanic Gardens, The Wirral)

Changes from the WeeWX-supplied Standard skin include:

- Javascript-based Archive file browser
- Larger charts
- click-to-enlarge charts
- colour-blind compatible chart line colours, based on http://jfly.iam.u-tokyo.ac.jp/color/ and http://www.cookbook-r.com/Graphs/Colors_%28ggplot2%29/#a-colorblind-friendly-palette

Requirements
============

You will need to download Jquery ( https://jquery.com/ ) and Jquery-UI (https://jqueryui.com/) for the Archive datepicker to work. (specifically, the WeeWX ``HTML_ROOT`` directory must have a subdirectory ``js`` with ``jquery.js`` and ``jquery-ui.js`` in and another subdirectory called ``css`` with ``jquery-ui.css`` in)

For the larger charts, your ``weewx.conf`` file need to include at least the 
``ImageGenerator`` section of the ``StandardReport`` section in the ``weewx.conf`` in this archive.

For the colour-blind compatible colours, ``weewx.conf`` needs the line beginning ``chart_line_colors`` in the ``ImageGenerator`` section. 
