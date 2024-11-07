# Scrapes colours product-based.

import requests
from bs4 import BeautifulSoup
import json

# Define the URL
html_content = '''

<!DOCTYPE html>
<html class="artistcolordata-page">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <meta name="description" content="The Most Precise Online Paint Mixer for Artist Colors. Accurately mix Artist Colors from RGB values, directly in your preferred browser! Try PaintMaker for FREE.">
    <meta name="keywords" content="RGB,CMYK,Paint,convert,mix,artist,colors,online">
    <title>Artist color data - SensualLogic</title>

    <link rel="icon" type="image/png" sizes="128x128" href="/images/favicon-128x128.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
    <link rel="mask-icon" href="/images/safari-pinned-tab.svg" color="#5bbad5">

    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&family=Yellowtail&display=swap">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css" integrity="sha384-XdYbMnZ/QjLh6iI4ogqCTaIjrFk87ip+ekIjefZch0Y+PvJ8CDYtEs1ipDmPorQ+" crossorigin="anonymous" type="text/css">
    
    
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous" type="text/css" media="screen">
        <link rel="stylesheet" href="/css/site.min.css?v=Al_iinmrULqtL6U3QGLThI74LVlkqsROoxCr2ZIpjwM" />
    

    

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-QWED00GJ6L"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'G-QWED00GJ6L');
    </script>
</head>
<body>

    <!-- Page -->
    <div id="page-wrapper" class="page-below-nav">

        <!-- Header -->
        <header id="header" class="navbar navbar-inverse navbar-fixed-top">
            <a class="navbar-brand" href="/"><span>sensual</span>logic</a>
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>
                <div class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="/paintmaker" title="PaintMaker">PaintMaker</a></li>
                        <li><a href="/apps" title="Apps">Apps</a></li>
                        <li class="dropdown">
                            <a data-toggle="dropdown" class="dropdown-toggle" href="#">Painters Tips <b class="caret"></b></a>
                            <ul class="dropdown-menu">
                                <li class="dropdown">
                                    <a data-toggle="dropdown" class="dropdown-toggle" href="#">Tips for PaintMaker</a>
                                    <ul class="dropdown-menu">
                                        <li><a href="http://sensuallogicarchive.dk/paintmaker/tips/before%20painting.html" target="_blank" title="Before Painting">Before Painting</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/paintmaker/tips/image%20paint%20check.html" target="_blank" title="Image Paint Check">Image Paint Check</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/paintmaker/the%20master&#x27;s%20palettes/index.html" target="_blank" title="Master&#x27;s Palettes">Master&#x27;s Palettes</a></li>
                                        <li class="current"><a href="/artistcolordata" title="Artist color RGB values">Artist color RGB values</a></li>
                                    </ul>
                                </li>
                                <li class="dropdown">
                                    <a data-toggle="dropdown" class="dropdown-toggle" href="#">Tips for Painters</a>
                                    <ul class="dropdown-menu">
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/blending%20brush%20technique.html" target="_blank" title="Blending brush technique">Blending brush technique</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/easy%20way%20to%20mount%20stretched%20canvas%20on%20wall.html" target="_blank" title="Easy way to mount a stretched canvas on wall">Easy way to mount a stretched canvas on wall</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/cleaning%20a%20brush.html" target="_blank" title="How to clean a brush">How to clean a brush</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/prepare%20paper%20for%20painting.html" target="_blank" title="How to prepare paper for painting">How to prepare paper for painting</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/how%20to%20stretch%20a%20canvas.html" target="_blank" title="How to stretch a canvas">How to stretch a canvas</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/image%20interpolation.html" target="_blank" title="Image interpolation">Image interpolation</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/inexpensive%20palette.html" target="_blank" title="Inexpensive palette">Inexpensive palette</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/splitting%20an%20image%20in%20photoshop.html" target="_blank" title="Splitting an image in Photoshop">Splitting an image in Photoshop</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/storing%20small%20amounts%20of%20paint.html" target="_blank" title="Storing small amounts of paint">Storing small amounts of paint</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/using%20a%20scale.html" target="_blank" title="Using a scale">Using a scale</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/using%20layers%20i%20photoshop%20for%20projecting.html" target="_blank" title="Using layers in Photoshop with a projector">Using layers in Photoshop with a projector</a></li>
                                        <li class="seperator"></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/colorcounter/index.html" target="_blank" title="ColorCounter">ColorCounter</a></li>
                                        <li><a href="http://sensuallogicarchive.dk/painters%20tools/imagedivider.html" target="_blank" title="ImageDivider">ImageDivider</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li class="dropdown">
                            <a data-toggle="dropdown" class="dropdown-toggle" href="#">Lab Images <b class="caret"></b></a>
                            <ul class="dropdown-menu">
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/winsor%20and%20newton%20artisan.html" target="_blank" title="Artisan - Winsor and Newton">Artisan - Winsor and Newton</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/winsor%20and%20newton%20artists%20oils.html" target="_blank" title="Artists Oils - Winsor and Newton">Artists Oils - Winsor and Newton</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/winsor%20and%20newton%20designer&#x27;s%20gouache.html" target="_blank" title="Designer&#x27;s Gouache - Winsor and Newton">Designer&#x27;s Gouache - Winsor and Newton</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/winsor%20%26%20newton&#x27;s%20galeria%20acrylic.html" target="_blank" title="Galeria Acrylic - Winsor &amp; Newton">Galeria Acrylic - Winsor &amp; Newton</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/golden%20heavy%20body%20acrylics.html" target="_blank" title="Golden Heavy Body Acrylics">Golden Heavy Body Acrylics</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/maimeri%20polycolor.html" target="_blank" title="PolyColor - Maimeri">PolyColor - Maimeri</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/schmincke%20primacryl.html" target="_blank" title="PrimaCryl - Schmincke">PrimaCryl - Schmincke</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/winsor%20and%20newton%20professional%20acrylics.html" target="_blank" title="Professional Acrylics - Winsor and Newton">Professional Acrylics - Winsor and Newton</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/rembrandt%20fine%20oil%20colours.html" target="_blank" title="Rembrandt Fine Oil Colours">Rembrandt Fine Oil Colours</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/daler%20rowney%20system%203.html" target="_blank" title="System 3 - Daler Rowney">System 3 - Daler Rowney</a></li>
                                <li><a href="http://sensuallogicarchive.dk/lab%20images/vallejo%20acrylic%20studio.html" target="_blank" title="Vallejo Acrylic Studio">Vallejo Acrylic Studio</a></li>
                            </ul>
                        </li>

                        <li><a href="/about" title="About">About</a></li>

                    </ul>
                    

    <ul class="nav navbar-nav navbar-right">
        <li><a data-modal="" href="/account/loginregister/2?returnurl=%2Fartistcolordata"><i class="fa fa-paper-plane fa-fw"></i><span>&nbsp; CREATE A FREE ACCOUNT</span></a></li>
        <li><a data-modal="" href="/account/loginregister/1?returnurl=%2Fartistcolordata"><i class="fa fa-user fa-fw"></i><span>&nbsp; LOG IN</span></a></li>
    </ul>

                </div>
            </div>
        </header>


        <!-- Main -->
        <article id="main" class="body-content container">
            


<img class="page-logo" src="/images/svg/chart.svg" />

<h1>Artist color data</h1>

<div class="info-box">
    <p style="display:none;">
        We have measured each pigments mass tone rgb value for all the paint sets below.<br\>

        When using physical paint it’s important to know how much light each pigment can reflect in order to adjust your images correctly on the computer before calculating recipes from them in PaintMaker.
        As an example the rgb value for red is 255, 0, 0 but a red pigment like Cadmium Red Light from Winsor & Newton Professional Acrylic has the rgb value 230,55,20. Pyrrole Red from the same set has rgb 193,0,28.
        As you can see what looks like very bright red in real life is not nearly as bright as a computer screen’s brightest red. This can be confusing since a red with rgb 193,0,28 on your screen doesn’t look anything near as bright as the Pyrrole pigment.

        Note: the adjustment default setting in PaintMaker take care of most color space/ gamut problems but once in a while you might need to adjust a color by hand. If that is the case use the desaturate option to further adjust a single pigment.

        We have measured each pigments mass tone rgb value for all the paint sets below.<br\>
        These RGB values ​​are measured with a spectrophotometer.<br\>
        The numbers show the color space limit of the artist colors.
    </p>
</div>

        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-0" data-toggle="collapse" data-target="#datapnl-0">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Artisan - Winsor &amp; Newton</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-0" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">74</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">58,22,14</td>
                                    <td style="background:rgb(58,22,14);width: 100px;">
                                    </td>
                                    <td class="center">1073</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">76</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">50,27,15</td>
                                    <td style="background:rgb(50,27,15);width: 100px;">
                                    </td>
                                    <td class="center">1346</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">90</td>
                                    <td>Cadmium Orange Hue</td>
                                    <td class="spaced">221,63,0</td>
                                    <td style="background:rgb(221,63,0);width: 100px;">
                                    </td>
                                    <td class="center">1338</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">98</td>
                                    <td>Cadmium Red Deep Hue</td>
                                    <td class="spaced">171,0,5</td>
                                    <td style="background:rgb(171,0,5);width: 100px;">
                                    </td>
                                    <td class="center">1302</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">99</td>
                                    <td>Cadmium Red Medium</td>
                                    <td class="spaced">221,63,0</td>
                                    <td style="background:rgb(221,63,0);width: 100px;">
                                    </td>
                                    <td class="center">1547</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">100</td>
                                    <td>Cadmium Red Light</td>
                                    <td class="spaced">229,42,0</td>
                                    <td style="background:rgb(229,42,0);width: 100px;">
                                    </td>
                                    <td class="center">1578</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">104</td>
                                    <td>Cadmium Red Dark</td>
                                    <td class="spaced">166,0,9</td>
                                    <td style="background:rgb(166,0,9);width: 100px;">
                                    </td>
                                    <td class="center">1455</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">109</td>
                                    <td>Cadmium Yellow Hue</td>
                                    <td class="spaced">255,139,0</td>
                                    <td style="background:rgb(255,139,0);width: 100px;">
                                    </td>
                                    <td class="center">1230</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">113</td>
                                    <td>Cadmium Yellow Light</td>
                                    <td class="spaced">255,194,0</td>
                                    <td style="background:rgb(255,194,0);width: 100px;">
                                    </td>
                                    <td class="center">1403</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">116</td>
                                    <td>Cadmium Yellow Medium</td>
                                    <td class="spaced">255,161,0</td>
                                    <td style="background:rgb(255,161,0);width: 100px;">
                                    </td>
                                    <td class="center">1534</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">137</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,97,102</td>
                                    <td style="background:rgb(0,97,102);width: 100px;">
                                    </td>
                                    <td class="center">1584</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">138</td>
                                    <td>Cerulean Blue Hue</td>
                                    <td class="spaced">0,74,91</td>
                                    <td style="background:rgb(0,74,91);width: 100px;">
                                    </td>
                                    <td class="center">1216</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">178</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">0,39,71</td>
                                    <td style="background:rgb(0,39,71);width: 100px;">
                                    </td>
                                    <td class="center">1264</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">229</td>
                                    <td>Dioxazine Purple</td>
                                    <td class="spaced">21,15,17</td>
                                    <td style="background:rgb(21,15,17);width: 100px;">
                                    </td>
                                    <td class="center">1268</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">263</td>
                                    <td>French Ultramarine</td>
                                    <td class="spaced">8,8,32</td>
                                    <td style="background:rgb(8,8,32);width: 100px;">
                                    </td>
                                    <td class="center">1277</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">331</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">27,28,28</td>
                                    <td style="background:rgb(27,28,28);width: 100px;">
                                    </td>
                                    <td class="center">1228</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">337</td>
                                    <td>Lamp Black</td>
                                    <td class="spaced">21,21,20</td>
                                    <td style="background:rgb(21,21,20);width: 100px;">
                                    </td>
                                    <td class="center">958</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">346</td>
                                    <td>Lemon Yellow</td>
                                    <td class="spaced">239,173,0</td>
                                    <td style="background:rgb(239,173,0);width: 100px;">
                                    </td>
                                    <td class="center">1024</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">380</td>
                                    <td>Magenta</td>
                                    <td class="spaced">98,4,32</td>
                                    <td style="background:rgb(98,4,32);width: 100px;">
                                    </td>
                                    <td class="center">1282</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">468</td>
                                    <td>Permanent Alizarin Crimson</td>
                                    <td class="spaced">74,1,16</td>
                                    <td style="background:rgb(74,1,16);width: 100px;">
                                    </td>
                                    <td class="center">1134</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">502</td>
                                    <td>Permanent Rose</td>
                                    <td class="spaced">130,0,24</td>
                                    <td style="background:rgb(130,0,24);width: 100px;">
                                    </td>
                                    <td class="center">1227</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">503</td>
                                    <td>Permanent Sap Green</td>
                                    <td class="spaced">28,42,10</td>
                                    <td style="background:rgb(28,42,10);width: 100px;">
                                    </td>
                                    <td class="center">1041</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">514</td>
                                    <td>Phthalo Blue (Red Shade)</td>
                                    <td class="spaced">17,12,37</td>
                                    <td style="background:rgb(17,12,37);width: 100px;">
                                    </td>
                                    <td class="center">1090</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">521</td>
                                    <td>Phthalo Green (Yellow Shade)</td>
                                    <td class="spaced">0,32,24</td>
                                    <td style="background:rgb(0,32,24);width: 100px;">
                                    </td>
                                    <td class="center">1091</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">522</td>
                                    <td>Phthalo Green (Blue Shade)</td>
                                    <td class="spaced">3,26,33</td>
                                    <td style="background:rgb(3,26,33);width: 100px;">
                                    </td>
                                    <td class="center">1021</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">538</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">15,11,11</td>
                                    <td style="background:rgb(15,11,11);width: 100px;">
                                    </td>
                                    <td class="center">984</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">552</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">117,70,17</td>
                                    <td style="background:rgb(117,70,17);width: 100px;">
                                    </td>
                                    <td class="center">1211</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">554</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">37,26,20</td>
                                    <td style="background:rgb(37,26,20);width: 100px;">
                                    </td>
                                    <td class="center">1273</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">644</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">249,245,234</td>
                                    <td style="background:rgb(249,245,234);width: 100px;">
                                    </td>
                                    <td class="center">1423</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">692</td>
                                    <td>Viridian</td>
                                    <td class="spaced">0,53,40</td>
                                    <td style="background:rgb(0,53,40);width: 100px;">
                                    </td>
                                    <td class="center">1149</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">744</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">187,128,18</td>
                                    <td style="background:rgb(187,128,18);width: 100px;">
                                    </td>
                                    <td class="center">1128</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">748</td>
                                    <td>Zinc White (Mixing White)</td>
                                    <td class="spaced">250,242,222</td>
                                    <td style="background:rgb(250,242,222);width: 100px;">
                                    </td>
                                    <td class="center">1687</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-1" data-toggle="collapse" data-target="#datapnl-1">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Artists Oil - Winsor &amp; Newton</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-1" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">4</td>
                                    <td>Alizarin Crimson</td>
                                    <td class="spaced">68,2,6</td>
                                    <td style="background:rgb(68,2,6);width: 100px;">
                                    </td>
                                    <td class="center">1045</td>
                                    <td class="center">T</td>
                                    <td class="center">B</td>
                                    <td class="center">PR83</td>
                                </tr>
                                <tr>
                                    <td class="center">25</td>
                                    <td>Bismuth Yellow</td>
                                    <td class="spaced">255,232,0</td>
                                    <td style="background:rgb(255,232,0);width: 100px;">
                                    </td>
                                    <td class="center">1684</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PY184</td>
                                </tr>
                                <tr>
                                    <td class="center">42</td>
                                    <td>Bright Red</td>
                                    <td class="spaced">197,0,15</td>
                                    <td style="background:rgb(197,0,15);width: 100px;">
                                    </td>
                                    <td class="center">1784</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PR</td>
                                </tr>
                                <tr>
                                    <td class="center">74</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">82,42,31</td>
                                    <td style="background:rgb(82,42,31);width: 100px;">
                                    </td>
                                    <td class="center">1181</td>
                                    <td class="center">T</td>
                                    <td class="center">AA</td>
                                    <td class="center">PR101</td>
                                </tr>
                                <tr>
                                    <td class="center">86</td>
                                    <td>Cadmium Lemon</td>
                                    <td class="spaced">255,222,0</td>
                                    <td style="background:rgb(255,222,0);width: 100px;">
                                    </td>
                                    <td class="center">2166</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PY35</td>
                                </tr>
                                <tr>
                                    <td class="center">94</td>
                                    <td>Cadmium Red</td>
                                    <td class="spaced">204,12,22</td>
                                    <td style="background:rgb(204,12,22);width: 100px;">
                                    </td>
                                    <td class="center">2199</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PR108</td>
                                </tr>
                                <tr>
                                    <td class="center">108</td>
                                    <td>Cadmium Yellow</td>
                                    <td class="spaced">255,164,0</td>
                                    <td style="background:rgb(255,164,0);width: 100px;">
                                    </td>
                                    <td class="center">1640</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PY35</td>
                                </tr>
                                <tr>
                                    <td class="center">111</td>
                                    <td>Cadmium Yellow Deep</td>
                                    <td class="spaced">255,127,15</td>
                                    <td style="background:rgb(255,127,15);width: 100px;">
                                    </td>
                                    <td class="center">2171</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PO20, PY35</td>
                                </tr>
                                <tr>
                                    <td class="center">137</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,100,160</td>
                                    <td style="background:rgb(0,100,160);width: 100px;">
                                    </td>
                                    <td class="center">2195</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">PB35</td>
                                </tr>
                                <tr>
                                    <td class="center">178</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">0,41,117</td>
                                    <td style="background:rgb(0,41,117);width: 100px;">
                                    </td>
                                    <td class="center">1495</td>
                                    <td class="center">ST</td>
                                    <td class="center">AA</td>
                                    <td class="center">PB28</td>
                                </tr>
                                <tr>
                                    <td class="center">180</td>
                                    <td>Cobalt Blue Deep</td>
                                    <td class="spaced">22,176,100</td>
                                    <td style="background:rgb(22,176,100);width: 100px;">
                                    </td>
                                    <td class="center">1871</td>
                                    <td class="center">ST</td>
                                    <td class="center">AA</td>
                                    <td class="center">PB74</td>
                                </tr>
                                <tr>
                                    <td class="center">183</td>
                                    <td>Cobalt Chromite Green</td>
                                    <td class="spaced">46,90,76</td>
                                    <td style="background:rgb(46,90,76);width: 100px;">
                                    </td>
                                    <td class="center">1749</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PG26</td>
                                </tr>
                                <tr>
                                    <td class="center">184</td>
                                    <td>Cobalt Green</td>
                                    <td class="spaced">0,123,110</td>
                                    <td style="background:rgb(0,123,110);width: 100px;">
                                    </td>
                                    <td class="center">1177</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">PG26, PG50</td>
                                </tr>
                                <tr>
                                    <td class="center">190</td>
                                    <td>Cobalt Turquoise</td>
                                    <td class="spaced">0,99,127</td>
                                    <td style="background:rgb(0,99,127);width: 100px;">
                                    </td>
                                    <td class="center">1841</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PB36</td>
                                </tr>
                                <tr>
                                    <td class="center">191</td>
                                    <td>Cobalt Turquoise Light</td>
                                    <td class="spaced">0,157,160</td>
                                    <td style="background:rgb(0,157,160);width: 100px;">
                                    </td>
                                    <td class="center">1685</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PG50</td>
                                </tr>
                                <tr>
                                    <td class="center">192</td>
                                    <td>Cobalt Violet</td>
                                    <td class="spaced">78,23,80</td>
                                    <td style="background:rgb(78,23,80);width: 100px;">
                                    </td>
                                    <td class="center">1605</td>
                                    <td class="center">ST</td>
                                    <td class="center">AA</td>
                                    <td class="center">PV14</td>
                                </tr>
                                <tr>
                                    <td class="center">263</td>
                                    <td>French Ultramarine</td>
                                    <td class="spaced">50,61,164</td>
                                    <td style="background:rgb(50,61,164);width: 100px;">
                                    </td>
                                    <td class="center">1397</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PB29</td>
                                </tr>
                                <tr>
                                    <td class="center">285</td>
                                    <td>Gold Ochre</td>
                                    <td class="spaced">168,113,37</td>
                                    <td style="background:rgb(168,113,37);width: 100px;">
                                    </td>
                                    <td class="center">1610</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY42</td>
                                </tr>
                                <tr>
                                    <td class="center">294</td>
                                    <td>Green Gold</td>
                                    <td class="spaced">71,74,14</td>
                                    <td style="background:rgb(71,74,14);width: 100px;">
                                    </td>
                                    <td class="center">1072</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PY129</td>
                                </tr>
                                <tr>
                                    <td class="center">319</td>
                                    <td>Indian Yellow</td>
                                    <td class="spaced">144,87,0</td>
                                    <td style="background:rgb(144,87,0);width: 100px;">
                                    </td>
                                    <td class="center">1506</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PY139, PR101</td>
                                </tr>
                                <tr>
                                    <td class="center">320</td>
                                    <td>Indian Yellow Deep</td>
                                    <td class="spaced">119,85,26</td>
                                    <td style="background:rgb(119,85,26);width: 100px;">
                                    </td>
                                    <td class="center">1150</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PY150</td>
                                </tr>
                                <tr>
                                    <td class="center">321</td>
                                    <td>Indanthrene Blue</td>
                                    <td class="spaced">33,23,57</td>
                                    <td style="background:rgb(33,23,57);width: 100px;">
                                    </td>
                                    <td class="center">1347</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PB60</td>
                                </tr>
                                <tr>
                                    <td class="center">331</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">16,15,17</td>
                                    <td style="background:rgb(16,15,17);width: 100px;">
                                    </td>
                                    <td class="center">1357</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBk9</td>
                                </tr>
                                <tr>
                                    <td class="center">337</td>
                                    <td>Lamp Black</td>
                                    <td class="spaced">26,27,27</td>
                                    <td style="background:rgb(26,27,27);width: 100px;">
                                    </td>
                                    <td class="center">965</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBk6</td>
                                </tr>
                                <tr>
                                    <td class="center">347</td>
                                    <td>Lemon Yellow Hue</td>
                                    <td class="spaced">235,215,84</td>
                                    <td style="background:rgb(235,215,84);width: 100px;">
                                    </td>
                                    <td class="center">1723</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY53</td>
                                </tr>
                                <tr>
                                    <td class="center">386</td>
                                    <td>Mars Black</td>
                                    <td class="spaced">39,38,39</td>
                                    <td style="background:rgb(39,38,39);width: 100px;">
                                    </td>
                                    <td class="center">2133</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBk11</td>
                                </tr>
                                <tr>
                                    <td class="center">425</td>
                                    <td>Naples Yellow Deep</td>
                                    <td class="spaced">222,156,72</td>
                                    <td style="background:rgb(222,156,72);width: 100px;">
                                    </td>
                                    <td class="center">1875</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBr24</td>
                                </tr>
                                <tr>
                                    <td class="center">426</td>
                                    <td>Naples Yellow Light</td>
                                    <td class="spaced">255,227,151</td>
                                    <td style="background:rgb(255,227,151);width: 100px;">
                                    </td>
                                    <td class="center">1970</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PW6, PY138, PO62</td>
                                </tr>
                                <tr>
                                    <td class="center">447</td>
                                    <td>Olive Green</td>
                                    <td class="spaced">47,43,32</td>
                                    <td style="background:rgb(47,43,32);width: 100px;">
                                    </td>
                                    <td class="center">1070</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PY110, PBk6</td>
                                </tr>
                                <tr>
                                    <td class="center">459</td>
                                    <td>Oxide of Chromium</td>
                                    <td class="spaced">57,95,58</td>
                                    <td style="background:rgb(57,95,58);width: 100px;">
                                    </td>
                                    <td class="center">2510</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PG17</td>
                                </tr>
                                <tr>
                                    <td class="center">468</td>
                                    <td>Permanent Alizarin Crimson</td>
                                    <td class="spaced">84,2,17</td>
                                    <td style="background:rgb(84,2,17);width: 100px;">
                                    </td>
                                    <td class="center">1157</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PR177</td>
                                </tr>
                                <tr>
                                    <td class="center">489</td>
                                    <td>Permanent Magenta</td>
                                    <td class="spaced">71,16,26</td>
                                    <td style="background:rgb(71,16,26);width: 100px;">
                                    </td>
                                    <td class="center">998</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PV19</td>
                                </tr>
                                <tr>
                                    <td class="center">491</td>
                                    <td>Permanent Mauve</td>
                                    <td class="spaced">68,50,73</td>
                                    <td style="background:rgb(68,50,73);width: 100px;">
                                    </td>
                                    <td class="center">1441</td>
                                    <td class="center">ST</td>
                                    <td class="center">AA</td>
                                    <td class="center">PV16</td>
                                </tr>
                                <tr>
                                    <td class="center">505</td>
                                    <td>Perylene Black</td>
                                    <td class="spaced">34,24,24</td>
                                    <td style="background:rgb(34,24,24);width: 100px;">
                                    </td>
                                    <td class="center">1065</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PBk31</td>
                                </tr>
                                <tr>
                                    <td class="center">538</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">18,28,41</td>
                                    <td style="background:rgb(18,28,41);width: 100px;">
                                    </td>
                                    <td class="center">1144</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PB27</td>
                                </tr>
                                <tr>
                                    <td class="center">545</td>
                                    <td>Quinacridone Magenta</td>
                                    <td class="spaced">108,8,36</td>
                                    <td style="background:rgb(108,8,36);width: 100px;">
                                    </td>
                                    <td class="center">1081</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PR122</td>
                                </tr>
                                <tr>
                                    <td class="center">548</td>
                                    <td>Quinacridone Red</td>
                                    <td class="spaced">144,32,40</td>
                                    <td style="background:rgb(144,32,40);width: 100px;">
                                    </td>
                                    <td class="center">1100</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PR209</td>
                                </tr>
                                <tr>
                                    <td class="center">552</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">130,83,39</td>
                                    <td style="background:rgb(130,83,39);width: 100px;">
                                    </td>
                                    <td class="center">1316</td>
                                    <td class="center">ST</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY43, PY42</td>
                                </tr>
                                <tr>
                                    <td class="center">554</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">64,49,35</td>
                                    <td style="background:rgb(64,49,35);width: 100px;">
                                    </td>
                                    <td class="center">1364</td>
                                    <td class="center">ST</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBr7</td>
                                </tr>
                                <tr>
                                    <td class="center">587</td>
                                    <td>Rose Madder Genuine</td>
                                    <td class="spaced">69,53,53</td>
                                    <td style="background:rgb(69,53,53);width: 100px;">
                                    </td>
                                    <td class="center">1222</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">NR9</td>
                                </tr>
                                <tr>
                                    <td class="center">599</td>
                                    <td>Sap Green</td>
                                    <td class="spaced"></td>
                                    <td style="background:rgb();width: 100px;">
                                    </td>
                                    <td class="center">27</td>
                                    <td class="center">44</td>
                                    <td class="center">20</td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">603</td>
                                    <td>Scarlet Lake</td>
                                    <td class="spaced">213,33,22</td>
                                    <td style="background:rgb(213,33,22);width: 100px;">
                                    </td>
                                    <td class="center">1096</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PR255</td>
                                </tr>
                                <tr>
                                    <td class="center">635</td>
                                    <td>Terra Rosa</td>
                                    <td class="spaced">146,75,63</td>
                                    <td style="background:rgb(146,75,63);width: 100px;">
                                    </td>
                                    <td class="center">1505</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PR101</td>
                                </tr>
                                <tr>
                                    <td class="center">637</td>
                                    <td>Terre Verte</td>
                                    <td class="spaced">38,59,47</td>
                                    <td style="background:rgb(38,59,47);width: 100px;">
                                    </td>
                                    <td class="center">1362</td>
                                    <td class="center">T</td>
                                    <td class="center">AA</td>
                                    <td class="center">PG23, PG18</td>
                                </tr>
                                <tr>
                                    <td class="center">644</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">251,250,241</td>
                                    <td style="background:rgb(251,250,241);width: 100px;">
                                    </td>
                                    <td class="center">1873</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PW6, PW4</td>
                                </tr>
                                <tr>
                                    <td class="center">647</td>
                                    <td>Transparent Red Ochre</td>
                                    <td class="spaced">149,66,40</td>
                                    <td style="background:rgb(149,66,40);width: 100px;">
                                    </td>
                                    <td class="center">1432</td>
                                    <td class="center">ST</td>
                                    <td class="center">AA</td>
                                    <td class="center">PR102</td>
                                </tr>
                                <tr>
                                    <td class="center">653</td>
                                    <td>Transparent Yellow</td>
                                    <td class="spaced">233,162,0</td>
                                    <td style="background:rgb(233,162,0);width: 100px;">
                                    </td>
                                    <td class="center">1093</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PY128</td>
                                </tr>
                                <tr>
                                    <td class="center">657</td>
                                    <td>Transparent Maroon</td>
                                    <td class="spaced">70,21,17</td>
                                    <td style="background:rgb(70,21,17);width: 100px;">
                                    </td>
                                    <td class="center">999</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PBr25</td>
                                </tr>
                                <tr>
                                    <td class="center">672</td>
                                    <td>Ultramarine Violet</td>
                                    <td class="spaced">62,38,126</td>
                                    <td style="background:rgb(62,38,126);width: 100px;">
                                    </td>
                                    <td class="center">1422</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PV15</td>
                                </tr>
                                <tr>
                                    <td class="center">676</td>
                                    <td>Vandyke Brown</td>
                                    <td class="spaced">39,27,19</td>
                                    <td style="background:rgb(39,27,19);width: 100px;">
                                    </td>
                                    <td class="center">1318</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">NBr8, PBr7</td>
                                </tr>
                                <tr>
                                    <td class="center">678</td>
                                    <td>Venetian Red</td>
                                    <td class="spaced">127,49,29</td>
                                    <td style="background:rgb(127,49,29);width: 100px;">
                                    </td>
                                    <td class="center">1677</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PR101</td>
                                </tr>
                                <tr>
                                    <td class="center">692</td>
                                    <td>Viridian</td>
                                    <td class="spaced">0,62,53</td>
                                    <td style="background:rgb(0,62,53);width: 100px;">
                                    </td>
                                    <td class="center">1360</td>
                                    <td class="center">T</td>
                                    <td class="center">AA</td>
                                    <td class="center">PG18</td>
                                </tr>
                                <tr>
                                    <td class="center">708</td>
                                    <td>Winsor Emerald</td>
                                    <td class="spaced">0,134,84</td>
                                    <td style="background:rgb(0,134,84);width: 100px;">
                                    </td>
                                    <td class="center">2143</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PG36, PW5</td>
                                </tr>
                                <tr>
                                    <td class="center">720</td>
                                    <td>Winsor Green (Phthalo)</td>
                                    <td class="spaced">0,50,40</td>
                                    <td style="background:rgb(0,50,40);width: 100px;">
                                    </td>
                                    <td class="center">1318</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PG7</td>
                                </tr>
                                <tr>
                                    <td class="center">721</td>
                                    <td>Winsor Green (Yellow shade)</td>
                                    <td class="spaced">0,60,33</td>
                                    <td style="background:rgb(0,60,33);width: 100px;">
                                    </td>
                                    <td class="center">1329</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PG36</td>
                                </tr>
                                <tr>
                                    <td class="center">722</td>
                                    <td>Winsor Lemon</td>
                                    <td class="spaced">248,65,0</td>
                                    <td style="background:rgb(248,65,0);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PY3</td>
                                </tr>
                                <tr>
                                    <td class="center">724</td>
                                    <td>Winsor Orange</td>
                                    <td class="spaced">129,0,24</td>
                                    <td style="background:rgb(129,0,24);width: 100px;">
                                    </td>
                                    <td class="center">1494</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PO73</td>
                                </tr>
                                <tr>
                                    <td class="center">725</td>
                                    <td>Winsor Red Deep</td>
                                    <td class="spaced">255,204,0</td>
                                    <td style="background:rgb(255,204,0);width: 100px;">
                                    </td>
                                    <td class="center">1517</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PR149</td>
                                </tr>
                                <tr>
                                    <td class="center">730</td>
                                    <td>Winsor Yellow</td>
                                    <td class="spaced">255,145,0</td>
                                    <td style="background:rgb(255,145,0);width: 100px;">
                                    </td>
                                    <td class="center">1380</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PY74</td>
                                </tr>
                                <tr>
                                    <td class="center">731</td>
                                    <td>Winsor Yellow Deep</td>
                                    <td class="spaced">29,23,41</td>
                                    <td style="background:rgb(29,23,41);width: 100px;">
                                    </td>
                                    <td class="center">1089</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PY65</td>
                                </tr>
                                <tr>
                                    <td class="center">733</td>
                                    <td>Winsor Violet (Dioxazine)</td>
                                    <td class="spaced">151,104,47</td>
                                    <td style="background:rgb(151,104,47);width: 100px;">
                                    </td>
                                    <td class="center">1060</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PV23</td>
                                </tr>
                                <tr>
                                    <td class="center">748</td>
                                    <td>Zinc White</td>
                                    <td class="spaced">249,248,235</td>
                                    <td style="background:rgb(249,248,235);width: 100px;">
                                    </td>
                                    <td class="center">2355</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PW4</td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-2" data-toggle="collapse" data-target="#datapnl-2">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Createx Airbrush Colors</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-2" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">5005</td>
                                    <td>Neutral Grey 5</td>
                                    <td class="spaced">144,152,156</td>
                                    <td style="background:rgb(144,152,156);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5016</td>
                                    <td>Light Olive Gold</td>
                                    <td class="spaced">172,132,104</td>
                                    <td style="background:rgb(172,132,104);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5017</td>
                                    <td>Olive Gold</td>
                                    <td class="spaced">164,129,99</td>
                                    <td style="background:rgb(164,129,99);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5018</td>
                                    <td>Deep Olive Gold</td>
                                    <td class="spaced">130,107,92</td>
                                    <td style="background:rgb(130,107,92);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5019</td>
                                    <td>Light Espresso</td>
                                    <td class="spaced">155,121,104</td>
                                    <td style="background:rgb(155,121,104);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5020</td>
                                    <td>Espresso</td>
                                    <td class="spaced">120,90,76</td>
                                    <td style="background:rgb(120,90,76);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5021</td>
                                    <td>Deep Espresso</td>
                                    <td class="spaced">100,74,66</td>
                                    <td style="background:rgb(100,74,66);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5022</td>
                                    <td>Fair Blush</td>
                                    <td class="spaced">215,178,163</td>
                                    <td style="background:rgb(215,178,163);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5023</td>
                                    <td>Blush</td>
                                    <td class="spaced">204,162,146</td>
                                    <td style="background:rgb(204,162,146);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5024</td>
                                    <td>Deep Blush</td>
                                    <td class="spaced">183,135,119</td>
                                    <td style="background:rgb(183,135,119);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5025</td>
                                    <td>Light Natural</td>
                                    <td class="spaced">218,199,186</td>
                                    <td style="background:rgb(218,199,186);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5026</td>
                                    <td>Natural</td>
                                    <td class="spaced">199,169,146</td>
                                    <td style="background:rgb(199,169,146);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5027</td>
                                    <td>Deep Natural</td>
                                    <td class="spaced">176,145,121</td>
                                    <td style="background:rgb(176,145,121);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5028</td>
                                    <td>Natural Lip</td>
                                    <td class="spaced">182,123,122</td>
                                    <td style="background:rgb(182,123,122);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5029</td>
                                    <td>Intrinsic Shade</td>
                                    <td class="spaced">116,100,114</td>
                                    <td style="background:rgb(116,100,114);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5030</td>
                                    <td>Cool Tone</td>
                                    <td class="spaced">76,139,136</td>
                                    <td style="background:rgb(76,139,136);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5035</td>
                                    <td>Old Bone White</td>
                                    <td class="spaced">242,236,206</td>
                                    <td style="background:rgb(242,236,206);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5036</td>
                                    <td>Dermatitus Tan</td>
                                    <td class="spaced">214,187,153</td>
                                    <td style="background:rgb(214,187,153);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5037</td>
                                    <td>Injury Ochre</td>
                                    <td class="spaced">133,94,41</td>
                                    <td style="background:rgb(133,94,41);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5038</td>
                                    <td>Infectious Pink</td>
                                    <td class="spaced">217,135,154</td>
                                    <td style="background:rgb(217,135,154);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5039</td>
                                    <td>Blood Red</td>
                                    <td class="spaced">119,47,47</td>
                                    <td style="background:rgb(119,47,47);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5040</td>
                                    <td>Coagulated Crimson</td>
                                    <td class="spaced">108,45,36</td>
                                    <td style="background:rgb(108,45,36);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5041</td>
                                    <td>Vascular Violet</td>
                                    <td class="spaced">61,52,50</td>
                                    <td style="background:rgb(61,52,50);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5042</td>
                                    <td>Deep Bruise Purple</td>
                                    <td class="spaced">68,57,57</td>
                                    <td style="background:rgb(68,57,57);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5043</td>
                                    <td>Expired Blue</td>
                                    <td class="spaced">69,116,137</td>
                                    <td style="background:rgb(69,116,137);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5044</td>
                                    <td>Code Blue</td>
                                    <td class="spaced">55,46,59</td>
                                    <td style="background:rgb(55,46,59);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5045</td>
                                    <td>Decay</td>
                                    <td class="spaced">64,62,60</td>
                                    <td style="background:rgb(64,62,60);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5046</td>
                                    <td>Blunt Trauma Umber</td>
                                    <td class="spaced">66,60,58</td>
                                    <td style="background:rgb(66,60,58);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5047</td>
                                    <td>Diseased Umber</td>
                                    <td class="spaced">62,60,58</td>
                                    <td style="background:rgb(62,60,58);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5048</td>
                                    <td>Surgery Sienna</td>
                                    <td class="spaced">87,60,43</td>
                                    <td style="background:rgb(87,60,43);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5049</td>
                                    <td>Vile Green</td>
                                    <td class="spaced">57,63,60</td>
                                    <td style="background:rgb(57,63,60);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5050</td>
                                    <td>White</td>
                                    <td class="spaced">249,251,247</td>
                                    <td style="background:rgb(249,251,247);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5051</td>
                                    <td>Black</td>
                                    <td class="spaced">68,66,63</td>
                                    <td style="background:rgb(68,66,63);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5052</td>
                                    <td>Yellow</td>
                                    <td class="spaced">243,175,0</td>
                                    <td style="background:rgb(243,175,0);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5053</td>
                                    <td>Scarlet</td>
                                    <td class="spaced">157,0,8</td>
                                    <td style="background:rgb(157,0,8);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5054</td>
                                    <td>Orange</td>
                                    <td class="spaced">183,50,14</td>
                                    <td style="background:rgb(183,50,14);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5055</td>
                                    <td>Violet</td>
                                    <td class="spaced">62,50,53</td>
                                    <td style="background:rgb(62,50,53);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5056</td>
                                    <td>Red Violet</td>
                                    <td class="spaced">76,58,65</td>
                                    <td style="background:rgb(76,58,65);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5057</td>
                                    <td>Blue Violet</td>
                                    <td class="spaced">65,54,62</td>
                                    <td style="background:rgb(65,54,62);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5058</td>
                                    <td>Viridian</td>
                                    <td class="spaced">38,59,61</td>
                                    <td style="background:rgb(38,59,61);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5059</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">60,46,69</td>
                                    <td style="background:rgb(60,46,69);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5060</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">63,45,80</td>
                                    <td style="background:rgb(63,45,80);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5061</td>
                                    <td>Magenta</td>
                                    <td class="spaced">84,0,35</td>
                                    <td style="background:rgb(84,0,35);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5062</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">51,52,55</td>
                                    <td style="background:rgb(51,52,55);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5063</td>
                                    <td>Sepia</td>
                                    <td class="spaced">57,55,51</td>
                                    <td style="background:rgb(57,55,51);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5064</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">101,61,50</td>
                                    <td style="background:rgb(101,61,50);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5065</td>
                                    <td>Moss Green</td>
                                    <td class="spaced">53,57,51</td>
                                    <td style="background:rgb(53,57,51);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5068</td>
                                    <td>Opaque White</td>
                                    <td class="spaced">252,254,249</td>
                                    <td style="background:rgb(252,254,249);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5069</td>
                                    <td>Opaque Yellow</td>
                                    <td class="spaced">255,237,47</td>
                                    <td style="background:rgb(255,237,47);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5070</td>
                                    <td> Opaque Chrome Yellow</td>
                                    <td class="spaced">255,167,22</td>
                                    <td style="background:rgb(255,167,22);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5071</td>
                                    <td>Opaque Orange</td>
                                    <td class="spaced">255,119,38</td>
                                    <td style="background:rgb(255,119,38);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5072</td>
                                    <td>Opaque Red Orange</td>
                                    <td class="spaced">227,74,63</td>
                                    <td style="background:rgb(227,74,63);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5073</td>
                                    <td>Opaque Red</td>
                                    <td class="spaced">189,48,59</td>
                                    <td style="background:rgb(189,48,59);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5073</td>
                                    <td>Opaque Red Grey</td>
                                    <td class="spaced"></td>
                                    <td style="background:rgb();width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5074</td>
                                    <td>Opaque Light Blue</td>
                                    <td class="spaced">70,111,204</td>
                                    <td style="background:rgb(70,111,204);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5075</td>
                                    <td> Opaque Dark Blue</td>
                                    <td class="spaced">68,57,96</td>
                                    <td style="background:rgb(68,57,96);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5076</td>
                                    <td>Opaque Purple</td>
                                    <td class="spaced">71,57,71</td>
                                    <td style="background:rgb(71,57,71);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5077</td>
                                    <td>Opaque Green</td>
                                    <td class="spaced">39,69,68</td>
                                    <td style="background:rgb(39,69,68);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5078</td>
                                    <td>Opaque Black</td>
                                    <td class="spaced">59,60,61</td>
                                    <td style="background:rgb(59,60,61);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5095</td>
                                    <td>Cyan CMYK</td>
                                    <td class="spaced">23,59,87</td>
                                    <td style="background:rgb(23,59,87);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5096</td>
                                    <td>Magenta CMYK</td>
                                    <td class="spaced">104,4,43</td>
                                    <td style="background:rgb(104,4,43);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5097</td>
                                    <td>Yellow CMYK</td>
                                    <td class="spaced">255,221,0</td>
                                    <td style="background:rgb(255,221,0);width: 100px;">
                                    </td>
                                    <td class="center">1000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-3" data-toggle="collapse" data-target="#datapnl-3">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Designers Gouache - Winsor &amp; Newton</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-3" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">4</td>
                                    <td>Alizarin Crimson</td>
                                    <td class="spaced">154,44,67</td>
                                    <td style="background:rgb(154,44,67);width: 100px;">
                                    </td>
                                    <td class="center">1478</td>
                                    <td class="center">SO</td>
                                    <td class="center">B</td>
                                    <td class="center">PR83</td>
                                </tr>
                                <tr>
                                    <td class="center">74</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">145,76,54</td>
                                    <td style="background:rgb(145,76,54);width: 100px;">
                                    </td>
                                    <td class="center">1762</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY42, PR101</td>
                                </tr>
                                <tr>
                                    <td class="center">76</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">104,72,61</td>
                                    <td style="background:rgb(104,72,61);width: 100px;">
                                    </td>
                                    <td class="center">1636</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBr7, PY42</td>
                                </tr>
                                <tr>
                                    <td class="center">86</td>
                                    <td>Cadmium Lemon</td>
                                    <td class="spaced">255,229,46</td>
                                    <td style="background:rgb(255,229,46);width: 100px;">
                                    </td>
                                    <td class="center">2240</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PY35</td>
                                </tr>
                                <tr>
                                    <td class="center">89</td>
                                    <td>Cadmium Orange</td>
                                    <td class="spaced">253,111,42</td>
                                    <td style="background:rgb(253,111,42);width: 100px;">
                                    </td>
                                    <td class="center">2740</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PY35, PR108</td>
                                </tr>
                                <tr>
                                    <td class="center">94</td>
                                    <td>Cadmium Red</td>
                                    <td class="spaced">210,59,55</td>
                                    <td style="background:rgb(210,59,55);width: 100px;">
                                    </td>
                                    <td class="center">2130</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PR108</td>
                                </tr>
                                <tr>
                                    <td class="center">106</td>
                                    <td>Cadmium Scarlet</td>
                                    <td class="spaced">233,69,47</td>
                                    <td style="background:rgb(233,69,47);width: 100px;">
                                    </td>
                                    <td class="center">1944</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PR108</td>
                                </tr>
                                <tr>
                                    <td class="center">108</td>
                                    <td>Cadmium Yellow</td>
                                    <td class="spaced">255,189,0</td>
                                    <td style="background:rgb(255,189,0);width: 100px;">
                                    </td>
                                    <td class="center">2069</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PY35, PO20</td>
                                </tr>
                                <tr>
                                    <td class="center">137</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">16,117,167</td>
                                    <td style="background:rgb(16,117,167);width: 100px;">
                                    </td>
                                    <td class="center">2585</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PB35</td>
                                </tr>
                                <tr>
                                    <td class="center">178</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">33,104,201</td>
                                    <td style="background:rgb(33,104,201);width: 100px;">
                                    </td>
                                    <td class="center">2662</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PB28</td>
                                </tr>
                                <tr>
                                    <td class="center">191</td>
                                    <td>Cobalt Turquoise Light</td>
                                    <td class="spaced">0,166,177</td>
                                    <td style="background:rgb(0,166,177);width: 100px;">
                                    </td>
                                    <td class="center">2233</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PG50</td>
                                </tr>
                                <tr>
                                    <td class="center">249</td>
                                    <td>Flame Red</td>
                                    <td class="spaced">210,64,53</td>
                                    <td style="background:rgb(210,64,53);width: 100px;">
                                    </td>
                                    <td class="center">1528</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PR170, PO72</td>
                                </tr>
                                <tr>
                                    <td class="center">322</td>
                                    <td>Indigo</td>
                                    <td class="spaced">56,59,88</td>
                                    <td style="background:rgb(56,59,88);width: 100px;">
                                    </td>
                                    <td class="center">1818</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PB15, PBk6, PB29</td>
                                </tr>
                                <tr>
                                    <td class="center">331</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">44,41,43</td>
                                    <td style="background:rgb(44,41,43);width: 100px;">
                                    </td>
                                    <td class="center">1811</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBk9</td>
                                </tr>
                                <tr>
                                    <td class="center">335</td>
                                    <td>Jet Black</td>
                                    <td class="spaced">39,33,35</td>
                                    <td style="background:rgb(39,33,35);width: 100px;">
                                    </td>
                                    <td class="center">1788</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PBk1</td>
                                </tr>
                                <tr>
                                    <td class="center">337</td>
                                    <td>Lamp Black</td>
                                    <td class="spaced">57,56,60</td>
                                    <td style="background:rgb(57,56,60);width: 100px;">
                                    </td>
                                    <td class="center">1478</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBk7</td>
                                </tr>
                                <tr>
                                    <td class="center">345</td>
                                    <td>Lemon Yellow</td>
                                    <td class="spaced">255,234,12</td>
                                    <td style="background:rgb(255,234,12);width: 100px;">
                                    </td>
                                    <td class="center">1542</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PY3</td>
                                </tr>
                                <tr>
                                    <td class="center">360</td>
                                    <td>Light Purple</td>
                                    <td class="spaced">115,57,152</td>
                                    <td style="background:rgb(115,57,152);width: 100px;">
                                    </td>
                                    <td class="center">1594</td>
                                    <td class="center">O</td>
                                    <td class="center">B</td>
                                    <td class="center">PV2, PV, 3</td>
                                </tr>
                                <tr>
                                    <td class="center">380</td>
                                    <td>Magenta</td>
                                    <td class="spaced">119,50,117</td>
                                    <td style="background:rgb(119,50,117);width: 100px;">
                                    </td>
                                    <td class="center">1618</td>
                                    <td class="center">ST</td>
                                    <td class="center">C</td>
                                    <td class="center">PR173, PV2</td>
                                </tr>
                                <tr>
                                    <td class="center">384</td>
                                    <td>Marigold Yellow</td>
                                    <td class="spaced">255,120,28</td>
                                    <td style="background:rgb(255,120,28);width: 100px;">
                                    </td>
                                    <td class="center">1545</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PO72, PO73</td>
                                </tr>
                                <tr>
                                    <td class="center">425</td>
                                    <td>Naples Yellow Deep</td>
                                    <td class="spaced">223,154,72</td>
                                    <td style="background:rgb(223,154,72);width: 100px;">
                                    </td>
                                    <td class="center">1509</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBr24</td>
                                </tr>
                                <tr>
                                    <td class="center">453</td>
                                    <td>Orange Lake Light</td>
                                    <td class="spaced">237,96,47</td>
                                    <td style="background:rgb(237,96,47);width: 100px;">
                                    </td>
                                    <td class="center">1710</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PY65, PR9</td>
                                </tr>
                                <tr>
                                    <td class="center">459</td>
                                    <td>Oxide of Chromium</td>
                                    <td class="spaced">78,107,82</td>
                                    <td style="background:rgb(78,107,82);width: 100px;">
                                    </td>
                                    <td class="center">2178</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PG17</td>
                                </tr>
                                <tr>
                                    <td class="center">466</td>
                                    <td>Permanent Alizarin Crimson</td>
                                    <td class="spaced">156,44,60</td>
                                    <td style="background:rgb(156,44,60);width: 100px;">
                                    </td>
                                    <td class="center">1489</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PR176</td>
                                </tr>
                                <tr>
                                    <td class="center">470</td>
                                    <td>Perylene Violet</td>
                                    <td class="spaced">76,53,66</td>
                                    <td style="background:rgb(76,53,66);width: 100px;">
                                    </td>
                                    <td class="center">1469</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PV29</td>
                                </tr>
                                <tr>
                                    <td class="center">502</td>
                                    <td>Permanent Rose</td>
                                    <td class="spaced">157,49,67</td>
                                    <td style="background:rgb(157,49,67);width: 100px;">
                                    </td>
                                    <td class="center">1759</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PV19</td>
                                </tr>
                                <tr>
                                    <td class="center">505</td>
                                    <td>Perylene Black</td>
                                    <td class="spaced">59,54,53</td>
                                    <td style="background:rgb(59,54,53);width: 100px;">
                                    </td>
                                    <td class="center">1405</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PBk31</td>
                                </tr>
                                <tr>
                                    <td class="center">507</td>
                                    <td>Perylene Maroon</td>
                                    <td class="spaced">125,54,69</td>
                                    <td style="background:rgb(125,54,69);width: 100px;">
                                    </td>
                                    <td class="center">1421</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PR179</td>
                                </tr>
                                <tr>
                                    <td class="center">508</td>
                                    <td>Permanent Yellow Deep</td>
                                    <td class="spaced">255,179,0</td>
                                    <td style="background:rgb(255,179,0);width: 100px;">
                                    </td>
                                    <td class="center">1495</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PY65</td>
                                </tr>
                                <tr>
                                    <td class="center">512</td>
                                    <td>Permanent White</td>
                                    <td class="spaced">255,245,251</td>
                                    <td style="background:rgb(255,245,251);width: 100px;">
                                    </td>
                                    <td class="center">2350</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PW6</td>
                                </tr>
                                <tr>
                                    <td class="center">523</td>
                                    <td>Primary Blue</td>
                                    <td class="spaced">0,128,203</td>
                                    <td style="background:rgb(0,128,203);width: 100px;">
                                    </td>
                                    <td class="center">1841</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PB15</td>
                                </tr>
                                <tr>
                                    <td class="center">524</td>
                                    <td>Primary Red</td>
                                    <td class="spaced">196,10,73</td>
                                    <td style="background:rgb(196,10,73);width: 100px;">
                                    </td>
                                    <td class="center">1540</td>
                                    <td class="center">SO</td>
                                    <td class="center">B</td>
                                    <td class="center">PR170</td>
                                </tr>
                                <tr>
                                    <td class="center">527</td>
                                    <td>Primary Yellow</td>
                                    <td class="spaced">255,222,0</td>
                                    <td style="background:rgb(255,222,0);width: 100px;">
                                    </td>
                                    <td class="center">1496</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PY74, PY138</td>
                                </tr>
                                <tr>
                                    <td class="center">538</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">27,64,111</td>
                                    <td style="background:rgb(27,64,111);width: 100px;">
                                    </td>
                                    <td class="center">1159</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PB27</td>
                                </tr>
                                <tr>
                                    <td class="center">552</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">191,119,66</td>
                                    <td style="background:rgb(191,119,66);width: 100px;">
                                    </td>
                                    <td class="center">1905</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY42, PR101, PY65</td>
                                </tr>
                                <tr>
                                    <td class="center">554</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">151,112,74</td>
                                    <td style="background:rgb(151,112,74);width: 100px;">
                                    </td>
                                    <td class="center">1694</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY42, PBr7</td>
                                </tr>
                                <tr>
                                    <td class="center">564</td>
                                    <td>Red Ochre</td>
                                    <td class="spaced">118,61,65</td>
                                    <td style="background:rgb(118,61,65);width: 100px;">
                                    </td>
                                    <td class="center">2322</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PR101, PV19</td>
                                </tr>
                                <tr>
                                    <td class="center">593</td>
                                    <td>Rose Tyrien</td>
                                    <td class="spaced">171,0,106</td>
                                    <td style="background:rgb(171,0,106);width: 100px;">
                                    </td>
                                    <td class="center">1480</td>
                                    <td class="center">SO</td>
                                    <td class="center">C</td>
                                    <td class="center">PR173</td>
                                </tr>
                                <tr>
                                    <td class="center">623</td>
                                    <td>Spectrum Red</td>
                                    <td class="spaced">173,60,65</td>
                                    <td style="background:rgb(173,60,65);width: 100px;">
                                    </td>
                                    <td class="center">1523</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PR170, PBr25</td>
                                </tr>
                                <tr>
                                    <td class="center">625</td>
                                    <td>Spectrum Violet</td>
                                    <td class="spaced">81,51,161</td>
                                    <td style="background:rgb(81,51,161);width: 100px;">
                                    </td>
                                    <td class="center">1549</td>
                                    <td class="center">O</td>
                                    <td class="center">B</td>
                                    <td class="center">PV3</td>
                                </tr>
                                <tr>
                                    <td class="center">660</td>
                                    <td>Ultramarine</td>
                                    <td class="spaced">49,52,174</td>
                                    <td style="background:rgb(49,52,174);width: 100px;">
                                    </td>
                                    <td class="center">2021</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PB29</td>
                                </tr>
                                <tr>
                                    <td class="center">667</td>
                                    <td>Ultramarine Green Shade</td>
                                    <td class="spaced">58,109,218</td>
                                    <td style="background:rgb(58,109,218);width: 100px;">
                                    </td>
                                    <td class="center">1692</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PB29</td>
                                </tr>
                                <tr>
                                    <td class="center">692</td>
                                    <td>Viridian</td>
                                    <td class="spaced">49,65,65</td>
                                    <td style="background:rgb(49,65,65);width: 100px;">
                                    </td>
                                    <td class="center">1667</td>
                                    <td class="center">T</td>
                                    <td class="center">AA</td>
                                    <td class="center">PG18</td>
                                </tr>
                                <tr>
                                    <td class="center">706</td>
                                    <td>Winsor Blue</td>
                                    <td class="spaced">62,50,87</td>
                                    <td style="background:rgb(62,50,87);width: 100px;">
                                    </td>
                                    <td class="center">1631</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PB15</td>
                                </tr>
                                <tr>
                                    <td class="center">720</td>
                                    <td>Winsor Green</td>
                                    <td class="spaced">30,83,74</td>
                                    <td style="background:rgb(30,83,74);width: 100px;">
                                    </td>
                                    <td class="center">1839</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PG7</td>
                                </tr>
                                <tr>
                                    <td class="center">733</td>
                                    <td>Winsor Violet (Dioxazine)</td>
                                    <td class="spaced">86,61,124</td>
                                    <td style="background:rgb(86,61,124);width: 100px;">
                                    </td>
                                    <td class="center">1574</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PV23</td>
                                </tr>
                                <tr>
                                    <td class="center">744</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">209,148,75</td>
                                    <td style="background:rgb(209,148,75);width: 100px;">
                                    </td>
                                    <td class="center">1799</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY42</td>
                                </tr>
                                <tr>
                                    <td class="center">748</td>
                                    <td>Zinc White</td>
                                    <td class="spaced">246,238,242</td>
                                    <td style="background:rgb(246,238,242);width: 100px;">
                                    </td>
                                    <td class="center">2904</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PW5</td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-4" data-toggle="collapse" data-target="#datapnl-4">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Ferrario1919 Oil - Ferrario</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-4" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">3</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">247,246,244</td>
                                    <td style="background:rgb(247,246,244);width: 100px;">
                                    </td>
                                    <td class="center">2175</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5</td>
                                    <td>Cadmium Yellow Lemon</td>
                                    <td class="spaced">251,211,0</td>
                                    <td style="background:rgb(251,211,0);width: 100px;">
                                    </td>
                                    <td class="center">2036</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">9</td>
                                    <td>Cadmium Yellow Light</td>
                                    <td class="spaced">255,196,0</td>
                                    <td style="background:rgb(255,196,0);width: 100px;">
                                    </td>
                                    <td class="center">2027</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">12</td>
                                    <td>Ferrario1919 Yellow Deep</td>
                                    <td class="spaced">255,151,0</td>
                                    <td style="background:rgb(255,151,0);width: 100px;">
                                    </td>
                                    <td class="center">1635</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">15</td>
                                    <td>Ferrario1919 Orange</td>
                                    <td class="spaced">255,115,0</td>
                                    <td style="background:rgb(255,115,0);width: 100px;">
                                    </td>
                                    <td class="center">1618</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">17</td>
                                    <td>Cadmium Red light</td>
                                    <td class="spaced">232,62,0</td>
                                    <td style="background:rgb(232,62,0);width: 100px;">
                                    </td>
                                    <td class="center">1985</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">21</td>
                                    <td>Ferrario1919 Red</td>
                                    <td class="spaced">192,0,0</td>
                                    <td style="background:rgb(192,0,0);width: 100px;">
                                    </td>
                                    <td class="center">1612</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">23</td>
                                    <td>Magenta</td>
                                    <td class="spaced">129,8,30</td>
                                    <td style="background:rgb(129,8,30);width: 100px;">
                                    </td>
                                    <td class="center">1603</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">26</td>
                                    <td>Alizarine Madder</td>
                                    <td class="spaced">89,0,17</td>
                                    <td style="background:rgb(89,0,17);width: 100px;">
                                    </td>
                                    <td class="center">1592</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">29</td>
                                    <td>Magenta Lake</td>
                                    <td class="spaced">115,0,30</td>
                                    <td style="background:rgb(115,0,30);width: 100px;">
                                    </td>
                                    <td class="center">1605</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">31</td>
                                    <td>Manganese Violet</td>
                                    <td class="spaced">69,22,75</td>
                                    <td style="background:rgb(69,22,75);width: 100px;">
                                    </td>
                                    <td class="center">1949</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">33</td>
                                    <td>Ultramarine Blue</td>
                                    <td class="spaced">11,8,34</td>
                                    <td style="background:rgb(11,8,34);width: 100px;">
                                    </td>
                                    <td class="center">1547</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">34</td>
                                    <td>Ultramarine Sky Blue</td>
                                    <td class="spaced">13,9,45</td>
                                    <td style="background:rgb(13,9,45);width: 100px;">
                                    </td>
                                    <td class="center">1553</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">36</td>
                                    <td>Ferrario1919 Blue - Red hue</td>
                                    <td class="spaced">13,16,48</td>
                                    <td style="background:rgb(13,16,48);width: 100px;">
                                    </td>
                                    <td class="center">1616</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">38</td>
                                    <td>Cobalt Blue light</td>
                                    <td class="spaced">0,150,165</td>
                                    <td style="background:rgb(0,150,165);width: 100px;">
                                    </td>
                                    <td class="center">2075</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">40</td>
                                    <td>Ferrario1919 Blue - Green hue</td>
                                    <td class="spaced">19,21,59</td>
                                    <td style="background:rgb(19,21,59);width: 100px;">
                                    </td>
                                    <td class="center">1656</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">41</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">11,16,36</td>
                                    <td style="background:rgb(11,16,36);width: 100px;">
                                    </td>
                                    <td class="center">1588</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">44</td>
                                    <td>Cerulean  Blue</td>
                                    <td class="spaced">0,98,146</td>
                                    <td style="background:rgb(0,98,146);width: 100px;">
                                    </td>
                                    <td class="center">2239</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">48</td>
                                    <td>Cobalt Turquoise</td>
                                    <td class="spaced">0,150,165</td>
                                    <td style="background:rgb(0,150,165);width: 100px;">
                                    </td>
                                    <td class="center">2175</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">49</td>
                                    <td>Cobalt Green Light</td>
                                    <td class="spaced">0,100,98</td>
                                    <td style="background:rgb(0,100,98);width: 100px;">
                                    </td>
                                    <td class="center">2249</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">51</td>
                                    <td>Ferrario1919 Green - Blue hue</td>
                                    <td class="spaced">0,34,35</td>
                                    <td style="background:rgb(0,34,35);width: 100px;">
                                    </td>
                                    <td class="center">1672</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">52</td>
                                    <td>Emerald Green</td>
                                    <td class="spaced">0,69,58</td>
                                    <td style="background:rgb(0,69,58);width: 100px;">
                                    </td>
                                    <td class="center">1627</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">53</td>
                                    <td>Ferrario1919 Green - Yellow hue</td>
                                    <td class="spaced">0,47,33</td>
                                    <td style="background:rgb(0,47,33);width: 100px;">
                                    </td>
                                    <td class="center">1706</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">55</td>
                                    <td>Permanent Green</td>
                                    <td class="spaced">0,112,58</td>
                                    <td style="background:rgb(0,112,58);width: 100px;">
                                    </td>
                                    <td class="center">2306</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">57</td>
                                    <td>Cadmium Green Light</td>
                                    <td class="spaced">118,198,0</td>
                                    <td style="background:rgb(118,198,0);width: 100px;">
                                    </td>
                                    <td class="center">2131</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">67</td>
                                    <td>Lemon Ochre</td>
                                    <td class="spaced">185,126,26</td>
                                    <td style="background:rgb(185,126,26);width: 100px;">
                                    </td>
                                    <td class="center">1528</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">71</td>
                                    <td>Transparent Mars Yellow</td>
                                    <td class="spaced">136,90,41</td>
                                    <td style="background:rgb(136,90,41);width: 100px;">
                                    </td>
                                    <td class="center">1768</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">83</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">42,27,18</td>
                                    <td style="background:rgb(42,27,18);width: 100px;">
                                    </td>
                                    <td class="center">1598</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">84</td>
                                    <td>Transparent Brown</td>
                                    <td class="spaced">51,22,13</td>
                                    <td style="background:rgb(51,22,13);width: 100px;">
                                    </td>
                                    <td class="center">1627</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">88</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">22,21,22</td>
                                    <td style="background:rgb(22,21,22);width: 100px;">
                                    </td>
                                    <td class="center">1475</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-5" data-toggle="collapse" data-target="#datapnl-5">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Galeria Acrylic - Winsor &amp; Newton</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-5" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">60</td>
                                    <td>Buff Titanium</td>
                                    <td class="spaced">224,186,144</td>
                                    <td style="background:rgb(224,186,144);width: 100px;">
                                    </td>
                                    <td class="center">1165</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PW6, PY42, PR101, PBk11</td>
                                </tr>
                                <tr>
                                    <td class="center">74</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">87,51,47</td>
                                    <td style="background:rgb(87,51,47);width: 100px;">
                                    </td>
                                    <td class="center">1023</td>
                                    <td class="center">T</td>
                                    <td class="center">AA</td>
                                    <td class="center">PR101, PY42, PBk11</td>
                                </tr>
                                <tr>
                                    <td class="center">76</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">73,57,55</td>
                                    <td style="background:rgb(73,57,55);width: 100px;">
                                    </td>
                                    <td class="center">1037</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBr7</td>
                                </tr>
                                <tr>
                                    <td class="center">95</td>
                                    <td>Cadmium Red Hue</td>
                                    <td class="spaced">190,37,37</td>
                                    <td style="background:rgb(190,37,37);width: 100px;">
                                    </td>
                                    <td class="center">993</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PR112</td>
                                </tr>
                                <tr>
                                    <td class="center">115</td>
                                    <td>Cadmium Yellow Deep Hue</td>
                                    <td class="spaced">255,161,0</td>
                                    <td style="background:rgb(255,161,0);width: 100px;">
                                    </td>
                                    <td class="center">1064</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PY65</td>
                                </tr>
                                <tr>
                                    <td class="center">120</td>
                                    <td>Cadmium Yellow Medium Hue</td>
                                    <td class="spaced">255,186,0</td>
                                    <td style="background:rgb(255,186,0);width: 100px;">
                                    </td>
                                    <td class="center">963</td>
                                    <td class="center">O</td>
                                    <td class="center">A</td>
                                    <td class="center">PY73, PY83</td>
                                </tr>
                                <tr>
                                    <td class="center">178</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">37,80,180</td>
                                    <td style="background:rgb(37,80,180);width: 100px;">
                                    </td>
                                    <td class="center">1117</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">N/A</td>
                                </tr>
                                <tr>
                                    <td class="center">203</td>
                                    <td>Crimson</td>
                                    <td class="spaced">167,1,33</td>
                                    <td style="background:rgb(167,1,33);width: 100px;">
                                    </td>
                                    <td class="center">1068</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PR170</td>
                                </tr>
                                <tr>
                                    <td class="center">294</td>
                                    <td>Green Gold</td>
                                    <td class="spaced">147,127,46</td>
                                    <td style="background:rgb(147,127,46);width: 100px;">
                                    </td>
                                    <td class="center">1100</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PY129</td>
                                </tr>
                                <tr>
                                    <td class="center">311</td>
                                    <td>Hooker&#x27;s Green</td>
                                    <td class="spaced">47,58,52</td>
                                    <td style="background:rgb(47,58,52);width: 100px;">
                                    </td>
                                    <td class="center">1086</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">PB15, PY83</td>
                                </tr>
                                <tr>
                                    <td class="center">331</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">43,41,44</td>
                                    <td style="background:rgb(43,41,44);width: 100px;">
                                    </td>
                                    <td class="center">991</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBk9</td>
                                </tr>
                                <tr>
                                    <td class="center">337</td>
                                    <td>Lamp Black</td>
                                    <td class="spaced">42,41,45</td>
                                    <td style="background:rgb(42,41,45);width: 100px;">
                                    </td>
                                    <td class="center">1121</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBk6</td>
                                </tr>
                                <tr>
                                    <td class="center">346</td>
                                    <td>Lemon Yellow</td>
                                    <td class="spaced">255,227,0</td>
                                    <td style="background:rgb(255,227,0);width: 100px;">
                                    </td>
                                    <td class="center">1083</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PY3</td>
                                </tr>
                                <tr>
                                    <td class="center">415</td>
                                    <td>Mixing White</td>
                                    <td class="spaced">255,247,254</td>
                                    <td style="background:rgb(255,247,254);width: 100px;">
                                    </td>
                                    <td class="center">1038</td>
                                    <td class="center">ST</td>
                                    <td class="center">AA</td>
                                    <td class="center">PW6</td>
                                </tr>
                                <tr>
                                    <td class="center">488</td>
                                    <td>Permanent Magenta</td>
                                    <td class="spaced">106,36,58</td>
                                    <td style="background:rgb(106,36,58);width: 100px;">
                                    </td>
                                    <td class="center">845</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PR122, PV19</td>
                                </tr>
                                <tr>
                                    <td class="center">522</td>
                                    <td>Phthalo Green</td>
                                    <td class="spaced">14,50,55</td>
                                    <td style="background:rgb(14,50,55);width: 100px;">
                                    </td>
                                    <td class="center">1079</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PG7</td>
                                </tr>
                                <tr>
                                    <td class="center">533</td>
                                    <td>Process Magenta</td>
                                    <td class="spaced">182,34,60</td>
                                    <td style="background:rgb(182,34,60);width: 100px;">
                                    </td>
                                    <td class="center">982</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PV19</td>
                                </tr>
                                <tr>
                                    <td class="center">535</td>
                                    <td>Process Cyan</td>
                                    <td class="spaced">26,54,118</td>
                                    <td style="background:rgb(26,54,118);width: 100px;">
                                    </td>
                                    <td class="center">1054</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PB15:3, PW6</td>
                                </tr>
                                <tr>
                                    <td class="center">537</td>
                                    <td>Process Yellow</td>
                                    <td class="spaced">255,200,0</td>
                                    <td style="background:rgb(255,200,0);width: 100px;">
                                    </td>
                                    <td class="center">984</td>
                                    <td class="center">ST</td>
                                    <td class="center">A</td>
                                    <td class="center">PY74</td>
                                </tr>
                                <tr>
                                    <td class="center">541</td>
                                    <td>Prussian Blue Hue</td>
                                    <td class="spaced">42,37,54</td>
                                    <td style="background:rgb(42,37,54);width: 100px;">
                                    </td>
                                    <td class="center">999</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PB29, PB15:3, PBk11</td>
                                </tr>
                                <tr>
                                    <td class="center">552</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">116,71,52</td>
                                    <td style="background:rgb(116,71,52);width: 100px;">
                                    </td>
                                    <td class="center">966</td>
                                    <td class="center">T</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY42, PR101, PBk9</td>
                                </tr>
                                <tr>
                                    <td class="center">554</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">65,53,46</td>
                                    <td style="background:rgb(65,53,46);width: 100px;">
                                    </td>
                                    <td class="center">1005</td>
                                    <td class="center">SO</td>
                                    <td class="center">AA</td>
                                    <td class="center">PBr7</td>
                                </tr>
                                <tr>
                                    <td class="center">564</td>
                                    <td>Red Ochre</td>
                                    <td class="spaced">126,43,36</td>
                                    <td style="background:rgb(126,43,36);width: 100px;">
                                    </td>
                                    <td class="center">975</td>
                                    <td class="center">N/A</td>
                                    <td class="center">AA</td>
                                    <td class="center">PR101</td>
                                </tr>
                                <tr>
                                    <td class="center">599</td>
                                    <td>Sap Green</td>
                                    <td class="spaced">51,100,58</td>
                                    <td style="background:rgb(51,100,58);width: 100px;">
                                    </td>
                                    <td class="center">1079</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PY14, PG7, PBk7, PW6</td>
                                </tr>
                                <tr>
                                    <td class="center">644</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">254,246,253</td>
                                    <td style="background:rgb(254,246,253);width: 100px;">
                                    </td>
                                    <td class="center">1185</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PW6</td>
                                </tr>
                                <tr>
                                    <td class="center">653</td>
                                    <td>Transparent Yellow</td>
                                    <td class="spaced">191,137,31</td>
                                    <td style="background:rgb(191,137,31);width: 100px;">
                                    </td>
                                    <td class="center">1099</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PY150, PY3</td>
                                </tr>
                                <tr>
                                    <td class="center">660</td>
                                    <td>Ultramarine</td>
                                    <td class="spaced">54,47,83</td>
                                    <td style="background:rgb(54,47,83);width: 100px;">
                                    </td>
                                    <td class="center">1060</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PB29</td>
                                </tr>
                                <tr>
                                    <td class="center">682</td>
                                    <td>Vermilion Hue</td>
                                    <td class="spaced">212,34,32</td>
                                    <td style="background:rgb(212,34,32);width: 100px;">
                                    </td>
                                    <td class="center">987</td>
                                    <td class="center">SO</td>
                                    <td class="center">A</td>
                                    <td class="center">PR9</td>
                                </tr>
                                <tr>
                                    <td class="center">728</td>
                                    <td>Winsor Violet</td>
                                    <td class="spaced">48,40,44</td>
                                    <td style="background:rgb(48,40,44);width: 100px;">
                                    </td>
                                    <td class="center">982</td>
                                    <td class="center">T</td>
                                    <td class="center">A</td>
                                    <td class="center">PV23, (RS)</td>
                                </tr>
                                <tr>
                                    <td class="center">744</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">188,134,61</td>
                                    <td style="background:rgb(188,134,61);width: 100px;">
                                    </td>
                                    <td class="center">870</td>
                                    <td class="center">O</td>
                                    <td class="center">AA</td>
                                    <td class="center">PY42, PW6, PBk11</td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-6" data-toggle="collapse" data-target="#datapnl-6">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Gamblin Artist Oil</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-6" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Ultramarine Blue</td>
                                    <td class="spaced">44,44,59</td>
                                    <td style="background:rgb(44,44,59);width: 100px;">
                                    </td>
                                    <td class="center">1847</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Lemon</td>
                                    <td class="spaced">253,221,0</td>
                                    <td style="background:rgb(253,221,0);width: 100px;">
                                    </td>
                                    <td class="center">2866</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Red Medium</td>
                                    <td class="spaced">198,53,58</td>
                                    <td style="background:rgb(198,53,58);width: 100px;">
                                    </td>
                                    <td class="center">2722</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">46,46,46</td>
                                    <td style="background:rgb(46,46,46);width: 100px;">
                                    </td>
                                    <td class="center">1884</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Mars Black</td>
                                    <td class="spaced">32,30,30</td>
                                    <td style="background:rgb(32,30,30);width: 100px;">
                                    </td>
                                    <td class="center">2782</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">53,36,30</td>
                                    <td style="background:rgb(53,36,30);width: 100px;">
                                    </td>
                                    <td class="center">1988</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">66,58,51</td>
                                    <td style="background:rgb(66,58,51);width: 100px;">
                                    </td>
                                    <td class="center">2537</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">102,62,54</td>
                                    <td style="background:rgb(102,62,54);width: 100px;">
                                    </td>
                                    <td class="center">2093</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">149,91,42</td>
                                    <td style="background:rgb(149,91,42);width: 100px;">
                                    </td>
                                    <td class="center">2240</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">180,124,48</td>
                                    <td style="background:rgb(180,124,48);width: 100px;">
                                    </td>
                                    <td class="center">2000</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Indian Red</td>
                                    <td class="spaced">110,45,40</td>
                                    <td style="background:rgb(110,45,40);width: 100px;">
                                    </td>
                                    <td class="center">2569</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Emerald Green</td>
                                    <td class="spaced">0,136,72</td>
                                    <td style="background:rgb(0,136,72);width: 100px;">
                                    </td>
                                    <td class="center">2077</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Viridian</td>
                                    <td class="spaced">24,72,62</td>
                                    <td style="background:rgb(24,72,62);width: 100px;">
                                    </td>
                                    <td class="center">1890</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cobalt Green</td>
                                    <td class="spaced">11,75,60</td>
                                    <td style="background:rgb(11,75,60);width: 100px;">
                                    </td>
                                    <td class="center">2863</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Phthalo Turquoise</td>
                                    <td class="spaced">6,26,37</td>
                                    <td style="background:rgb(6,26,37);width: 100px;">
                                    </td>
                                    <td class="center">1906</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cobalt Teal</td>
                                    <td class="spaced">4,183,180</td>
                                    <td style="background:rgb(4,183,180);width: 100px;">
                                    </td>
                                    <td class="center">2538</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Manganese Blue Hue</td>
                                    <td class="spaced">26,74,98</td>
                                    <td style="background:rgb(26,74,98);width: 100px;">
                                    </td>
                                    <td class="center">2070</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,97,140</td>
                                    <td style="background:rgb(0,97,140);width: 100px;">
                                    </td>
                                    <td class="center">2800</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">0,45,109</td>
                                    <td style="background:rgb(0,45,109);width: 100px;">
                                    </td>
                                    <td class="center">2308</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Phthalo Blue</td>
                                    <td class="spaced">17,13,36</td>
                                    <td style="background:rgb(17,13,36);width: 100px;">
                                    </td>
                                    <td class="center">1684</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Indanthrone Blue</td>
                                    <td class="spaced">50,46,52</td>
                                    <td style="background:rgb(50,46,52);width: 100px;">
                                    </td>
                                    <td class="center">1916</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">13,11,12</td>
                                    <td style="background:rgb(13,11,12);width: 100px;">
                                    </td>
                                    <td class="center">1772</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Manganese Violet</td>
                                    <td class="spaced">60,15,56</td>
                                    <td style="background:rgb(60,15,56);width: 100px;">
                                    </td>
                                    <td class="center">2073</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Dioxazine Purple</td>
                                    <td class="spaced">38,32,33</td>
                                    <td style="background:rgb(38,32,33);width: 100px;">
                                    </td>
                                    <td class="center">1880</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cobalt Violet</td>
                                    <td class="spaced">70,27,72</td>
                                    <td style="background:rgb(70,27,72);width: 100px;">
                                    </td>
                                    <td class="center">2425</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Quinacridone Violet</td>
                                    <td class="spaced">85,20,34</td>
                                    <td style="background:rgb(85,20,34);width: 100px;">
                                    </td>
                                    <td class="center">1705</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Quinacridone Magenta</td>
                                    <td class="spaced">97,18,41</td>
                                    <td style="background:rgb(97,18,41);width: 100px;">
                                    </td>
                                    <td class="center">1738</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Phthalo Emerald</td>
                                    <td class="spaced">0,36,29</td>
                                    <td style="background:rgb(0,36,29);width: 100px;">
                                    </td>
                                    <td class="center">1903</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Chromium Oxide Green</td>
                                    <td class="spaced">76,109,73</td>
                                    <td style="background:rgb(76,109,73);width: 100px;">
                                    </td>
                                    <td class="center">2869</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Yellow Deep</td>
                                    <td class="spaced">255,165,0</td>
                                    <td style="background:rgb(255,165,0);width: 100px;">
                                    </td>
                                    <td class="center">2620</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Permanent Green Light</td>
                                    <td class="spaced">35,150,0</td>
                                    <td style="background:rgb(35,150,0);width: 100px;">
                                    </td>
                                    <td class="center">1723</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Yellow Medium</td>
                                    <td class="spaced">255,184,0</td>
                                    <td style="background:rgb(255,184,0);width: 100px;">
                                    </td>
                                    <td class="center">2665</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Yellow Light</td>
                                    <td class="spaced">254,217,0</td>
                                    <td style="background:rgb(254,217,0);width: 100px;">
                                    </td>
                                    <td class="center">2606</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Hansa Yellow Light</td>
                                    <td class="spaced">241,203,0</td>
                                    <td style="background:rgb(241,203,0);width: 100px;">
                                    </td>
                                    <td class="center">1645</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Orange</td>
                                    <td class="spaced">255,126,0</td>
                                    <td style="background:rgb(255,126,0);width: 100px;">
                                    </td>
                                    <td class="center">3022</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Orange Deep</td>
                                    <td class="spaced">243,91,23</td>
                                    <td style="background:rgb(243,91,23);width: 100px;">
                                    </td>
                                    <td class="center">2889</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Red Light</td>
                                    <td class="spaced">220,50,40</td>
                                    <td style="background:rgb(220,50,40);width: 100px;">
                                    </td>
                                    <td class="center">2798</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Napthol Scarlet</td>
                                    <td class="spaced">191,40,26</td>
                                    <td style="background:rgb(191,40,26);width: 100px;">
                                    </td>
                                    <td class="center">1816</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Perylene Red</td>
                                    <td class="spaced">99,0,7</td>
                                    <td style="background:rgb(99,0,7);width: 100px;">
                                    </td>
                                    <td class="center">1585</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Red Deep</td>
                                    <td class="spaced">165,45,56</td>
                                    <td style="background:rgb(165,45,56);width: 100px;">
                                    </td>
                                    <td class="center">2768</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Quinacridone Red</td>
                                    <td class="spaced">138,25,42</td>
                                    <td style="background:rgb(138,25,42);width: 100px;">
                                    </td>
                                    <td class="center">1811</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Alizarin Crimson</td>
                                    <td class="spaced">72,28,31</td>
                                    <td style="background:rgb(72,28,31);width: 100px;">
                                    </td>
                                    <td class="center">1595</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Naphtol Red</td>
                                    <td class="spaced">191,3,0</td>
                                    <td style="background:rgb(191,3,0);width: 100px;">
                                    </td>
                                    <td class="center">1817</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">248,245,237</td>
                                    <td style="background:rgb(248,245,237);width: 100px;">
                                    </td>
                                    <td class="center">2659</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Titanium Buff</td>
                                    <td class="spaced">203,181,139</td>
                                    <td style="background:rgb(203,181,139);width: 100px;">
                                    </td>
                                    <td class="center">2509</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-7" data-toggle="collapse" data-target="#datapnl-7">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Golden Heavy Body Acrylic</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-7" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">1010</td>
                                    <td>Bone Black</td>
                                    <td class="spaced">35,34,36</td>
                                    <td style="background:rgb(35,34,36);width: 100px;">
                                    </td>
                                    <td class="center">976</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1020</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">112,62,53</td>
                                    <td style="background:rgb(112,62,53);width: 100px;">
                                    </td>
                                    <td class="center">1111</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1030</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">70,56,54</td>
                                    <td style="background:rgb(70,56,54);width: 100px;">
                                    </td>
                                    <td class="center">1038</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1040</td>
                                    <td>Carbon Black</td>
                                    <td class="spaced">30,29,31</td>
                                    <td style="background:rgb(30,29,31);width: 100px;">
                                    </td>
                                    <td class="center">925</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1050</td>
                                    <td>Cerulean Blue Chromium</td>
                                    <td class="spaced">0,85,152</td>
                                    <td style="background:rgb(0,85,152);width: 100px;">
                                    </td>
                                    <td class="center">1104</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1060</td>
                                    <td>Chromium Oxide Green</td>
                                    <td class="spaced">76,106,67</td>
                                    <td style="background:rgb(76,106,67);width: 100px;">
                                    </td>
                                    <td class="center">1038</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1070</td>
                                    <td>C.P. Cadmium Orange</td>
                                    <td class="spaced">255,99,0</td>
                                    <td style="background:rgb(255,99,0);width: 100px;">
                                    </td>
                                    <td class="center">1044</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1090</td>
                                    <td>C.P. Cadmium Red Light</td>
                                    <td class="spaced">227,40,16</td>
                                    <td style="background:rgb(227,40,16);width: 100px;">
                                    </td>
                                    <td class="center">1125</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1100</td>
                                    <td>C.P. Cadmium Red Medium</td>
                                    <td class="spaced">185,5,32</td>
                                    <td style="background:rgb(185,5,32);width: 100px;">
                                    </td>
                                    <td class="center">1089</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1130</td>
                                    <td>C.P. Cadmium Yellow Med</td>
                                    <td class="spaced">255,200,0</td>
                                    <td style="background:rgb(255,200,0);width: 100px;">
                                    </td>
                                    <td class="center">1115</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1135</td>
                                    <td>C.P. Cadmium Yellow Primrose</td>
                                    <td class="spaced">249,231,20</td>
                                    <td style="background:rgb(249,231,20);width: 100px;">
                                    </td>
                                    <td class="center">1065</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1140</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">8,50,160</td>
                                    <td style="background:rgb(8,50,160);width: 100px;">
                                    </td>
                                    <td class="center">1078</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1147</td>
                                    <td>Diarylide Yellow</td>
                                    <td class="spaced">255,162,0</td>
                                    <td style="background:rgb(255,162,0);width: 100px;">
                                    </td>
                                    <td class="center">911</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1150</td>
                                    <td>Dioxazine Purple</td>
                                    <td class="spaced">25,17,19</td>
                                    <td style="background:rgb(25,17,19);width: 100px;">
                                    </td>
                                    <td class="center">912</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1180</td>
                                    <td>Hansa Yellow Light</td>
                                    <td class="spaced">250,226,0</td>
                                    <td style="background:rgb(250,226,0);width: 100px;">
                                    </td>
                                    <td class="center">950</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1225</td>
                                    <td>Nickel Azo Yellow</td>
                                    <td class="spaced">126,93,9</td>
                                    <td style="background:rgb(126,93,9);width: 100px;">
                                    </td>
                                    <td class="center">915</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1255</td>
                                    <td>Phthalo Blue / G.S.</td>
                                    <td class="spaced">16,3,62</td>
                                    <td style="background:rgb(16,3,62);width: 100px;">
                                    </td>
                                    <td class="center">901</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1270</td>
                                    <td>Phthalo Green / B.S.</td>
                                    <td class="spaced">0,31,41</td>
                                    <td style="background:rgb(0,31,41);width: 100px;">
                                    </td>
                                    <td class="center">915</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1275</td>
                                    <td>Phthalo Green / Y.S.</td>
                                    <td class="spaced">0,31,27</td>
                                    <td style="background:rgb(0,31,27);width: 100px;">
                                    </td>
                                    <td class="center">922</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1276</td>
                                    <td>Pyrrole Orange</td>
                                    <td class="spaced">239,61,0</td>
                                    <td style="background:rgb(239,61,0);width: 100px;">
                                    </td>
                                    <td class="center">905</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1277</td>
                                    <td>Pyrrole Red</td>
                                    <td class="spaced">187,0,0</td>
                                    <td style="background:rgb(187,0,0);width: 100px;">
                                    </td>
                                    <td class="center">950</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1305</td>
                                    <td>Quinacridone Magenta</td>
                                    <td class="spaced">90,0,37</td>
                                    <td style="background:rgb(90,0,37);width: 100px;">
                                    </td>
                                    <td class="center">911</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1310</td>
                                    <td>Quinacridone Red</td>
                                    <td class="spaced">150,0,37</td>
                                    <td style="background:rgb(150,0,37);width: 100px;">
                                    </td>
                                    <td class="center">924</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1340</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">157,103,52</td>
                                    <td style="background:rgb(157,103,52);width: 100px;">
                                    </td>
                                    <td class="center">1066</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1350</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">64,56,54</td>
                                    <td style="background:rgb(64,56,54);width: 100px;">
                                    </td>
                                    <td class="center">804</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1360</td>
                                    <td>Red Oxide</td>
                                    <td class="spaced">132,53,41</td>
                                    <td style="background:rgb(132,53,41);width: 100px;">
                                    </td>
                                    <td class="center">1124</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1370</td>
                                    <td>Titan Buff</td>
                                    <td class="spaced">225,205,186</td>
                                    <td style="background:rgb(225,205,186);width: 100px;">
                                    </td>
                                    <td class="center">1122</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1380</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">255,247,255</td>
                                    <td style="background:rgb(255,247,255);width: 100px;">
                                    </td>
                                    <td class="center">1179</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1400</td>
                                    <td>Ultramarine Blue</td>
                                    <td class="spaced">50,47,75</td>
                                    <td style="background:rgb(50,47,75);width: 100px;">
                                    </td>
                                    <td class="center">1054</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1401</td>
                                    <td>Ultramarine Violet</td>
                                    <td class="spaced">54,47,75</td>
                                    <td style="background:rgb(54,47,75);width: 100px;">
                                    </td>
                                    <td class="center">1048</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1407</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">186,124,51</td>
                                    <td style="background:rgb(186,124,51);width: 100px;">
                                    </td>
                                    <td class="center">1019</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1445</td>
                                    <td>Natural Gray N5</td>
                                    <td class="spaced">120,116,122</td>
                                    <td style="background:rgb(120,116,122);width: 100px;">
                                    </td>
                                    <td class="center">1086</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1500</td>
                                    <td>Primary Cyan</td>
                                    <td class="spaced">0,63,130</td>
                                    <td style="background:rgb(0,63,130);width: 100px;">
                                    </td>
                                    <td class="center">936</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1510</td>
                                    <td>Primary Magenta</td>
                                    <td class="spaced">169,26,49</td>
                                    <td style="background:rgb(169,26,49);width: 100px;">
                                    </td>
                                    <td class="center">922</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">1530</td>
                                    <td>Primary Yellow</td>
                                    <td class="spaced">255,215,0</td>
                                    <td style="background:rgb(255,215,0);width: 100px;">
                                    </td>
                                    <td class="center">947</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-8" data-toggle="collapse" data-target="#datapnl-8">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Grumbacher Max Water Mixable Oil</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-8" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Alizarin Crimson</td>
                                    <td class="spaced">78,3,23</td>
                                    <td style="background:rgb(78,3,23);width: 100px;">
                                    </td>
                                    <td class="center">1447</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">23</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">103,47,33</td>
                                    <td style="background:rgb(103,47,33);width: 100px;">
                                    </td>
                                    <td class="center">1757</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">24</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">44,33,24</td>
                                    <td style="background:rgb(44,33,24);width: 100px;">
                                    </td>
                                    <td class="center">1670</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">25</td>
                                    <td>Cadmium-Barium Orange</td>
                                    <td class="spaced">251,97,0</td>
                                    <td style="background:rgb(251,97,0);width: 100px;">
                                    </td>
                                    <td class="center">2378</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">26</td>
                                    <td>Cadmium-Barium Red Deep</td>
                                    <td class="spaced">144,42,53</td>
                                    <td style="background:rgb(144,42,53);width: 100px;">
                                    </td>
                                    <td class="center">2499</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">27</td>
                                    <td>Cadmium-Barium Red Light</td>
                                    <td class="spaced">215,45,44</td>
                                    <td style="background:rgb(215,45,44);width: 100px;">
                                    </td>
                                    <td class="center">2579</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">29</td>
                                    <td>Cadmium-Barium Red Med</td>
                                    <td class="spaced">167,0,12</td>
                                    <td style="background:rgb(167,0,12);width: 100px;">
                                    </td>
                                    <td class="center">2517</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">30</td>
                                    <td>Cadmiium-Barium Red Vermillion</td>
                                    <td class="spaced">196,50,58</td>
                                    <td style="background:rgb(196,50,58);width: 100px;">
                                    </td>
                                    <td class="center">2530</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">31</td>
                                    <td>Cadmium-Barium Yellow Deep</td>
                                    <td class="spaced">255,156,0</td>
                                    <td style="background:rgb(255,156,0);width: 100px;">
                                    </td>
                                    <td class="center">2431</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">33</td>
                                    <td>Cadmium-Barium Yellow Light</td>
                                    <td class="spaced">254,188,0</td>
                                    <td style="background:rgb(254,188,0);width: 100px;">
                                    </td>
                                    <td class="center">2354</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">34</td>
                                    <td>Cadmium-Barium Yellow Med</td>
                                    <td class="spaced">255,158,0</td>
                                    <td style="background:rgb(255,158,0);width: 100px;">
                                    </td>
                                    <td class="center">2504</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">36</td>
                                    <td>Cadmium-Barium Yellow Pale</td>
                                    <td class="spaced">254,221,0</td>
                                    <td style="background:rgb(254,221,0);width: 100px;">
                                    </td>
                                    <td class="center">2654</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">40</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,89,132</td>
                                    <td style="background:rgb(0,89,132);width: 100px;">
                                    </td>
                                    <td class="center">2498</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">48</td>
                                    <td>Chromium Oxide Green</td>
                                    <td class="spaced">67,101,66</td>
                                    <td style="background:rgb(67,101,66);width: 100px;">
                                    </td>
                                    <td class="center">3024</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">49</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">0,46,85</td>
                                    <td style="background:rgb(0,46,85);width: 100px;">
                                    </td>
                                    <td class="center">1842</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">60</td>
                                    <td>Diarylide Yellow</td>
                                    <td class="spaced">255,136,0</td>
                                    <td style="background:rgb(255,136,0);width: 100px;">
                                    </td>
                                    <td class="center">1435</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">61</td>
                                    <td>Dioxazine Purple</td>
                                    <td class="spaced">31,26,23</td>
                                    <td style="background:rgb(31,26,23);width: 100px;">
                                    </td>
                                    <td class="center">1660</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">76</td>
                                    <td>French Ultramarine Blue</td>
                                    <td class="spaced">13,13,32</td>
                                    <td style="background:rgb(13,13,32);width: 100px;">
                                    </td>
                                    <td class="center">1683</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">95</td>
                                    <td>Grumbacher Red</td>
                                    <td class="spaced">196,15,0</td>
                                    <td style="background:rgb(196,15,0);width: 100px;">
                                    </td>
                                    <td class="center">1660</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">109</td>
                                    <td>Indanthrone Blue</td>
                                    <td class="spaced">31,26,38</td>
                                    <td style="background:rgb(31,26,38);width: 100px;">
                                    </td>
                                    <td class="center">1467</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">115</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">47,46,46</td>
                                    <td style="background:rgb(47,46,46);width: 100px;">
                                    </td>
                                    <td class="center">1758</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">116</td>
                                    <td>Lamp Black</td>
                                    <td class="spaced">43,45,47</td>
                                    <td style="background:rgb(43,45,47);width: 100px;">
                                    </td>
                                    <td class="center">1262</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">134</td>
                                    <td>Mars Black</td>
                                    <td class="spaced">34,33,33</td>
                                    <td style="background:rgb(34,33,33);width: 100px;">
                                    </td>
                                    <td class="center">2330</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">146</td>
                                    <td>Naples Yellow</td>
                                    <td class="spaced">235,176,89</td>
                                    <td style="background:rgb(235,176,89);width: 100px;">
                                    </td>
                                    <td class="center">2769</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">160</td>
                                    <td>Permanent Blue</td>
                                    <td class="spaced">20,22,34</td>
                                    <td style="background:rgb(20,22,34);width: 100px;">
                                    </td>
                                    <td class="center">1648</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">163</td>
                                    <td>Perylene Maroon</td>
                                    <td class="spaced">98,28,40</td>
                                    <td style="background:rgb(98,28,40);width: 100px;">
                                    </td>
                                    <td class="center">1455</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">166</td>
                                    <td>Prussian Green</td>
                                    <td class="spaced">18,36,30</td>
                                    <td style="background:rgb(18,36,30);width: 100px;">
                                    </td>
                                    <td class="center">1526</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">168</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">23,18,12</td>
                                    <td style="background:rgb(23,18,12);width: 100px;">
                                    </td>
                                    <td class="center">1550</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">169</td>
                                    <td>Quinacridone Orange</td>
                                    <td class="spaced">67,21,11</td>
                                    <td style="background:rgb(67,21,11);width: 100px;">
                                    </td>
                                    <td class="center">1362</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">170</td>
                                    <td>Quinacridone Red</td>
                                    <td class="spaced">162,0,28</td>
                                    <td style="background:rgb(162,0,28);width: 100px;">
                                    </td>
                                    <td class="center">1501</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">171</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">151,92,42</td>
                                    <td style="background:rgb(151,92,42);width: 100px;">
                                    </td>
                                    <td class="center">2036</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">172</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">52,44,34</td>
                                    <td style="background:rgb(52,44,34);width: 100px;">
                                    </td>
                                    <td class="center">1715</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">187</td>
                                    <td>Sap Green</td>
                                    <td class="spaced">19,33,20</td>
                                    <td style="background:rgb(19,33,20);width: 100px;">
                                    </td>
                                    <td class="center">1590</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">203</td>
                                    <td>Thalo Blue</td>
                                    <td class="spaced">25,12,50</td>
                                    <td style="background:rgb(25,12,50);width: 100px;">
                                    </td>
                                    <td class="center">1335</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">205</td>
                                    <td>Thalo Green BS</td>
                                    <td class="spaced">0,37,34</td>
                                    <td style="background:rgb(0,37,34);width: 100px;">
                                    </td>
                                    <td class="center">1583</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">208</td>
                                    <td>Thalo Red Rose</td>
                                    <td class="spaced">136,0,22</td>
                                    <td style="background:rgb(136,0,22);width: 100px;">
                                    </td>
                                    <td class="center">1569</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">210</td>
                                    <td>Thalo Yellow Green</td>
                                    <td class="spaced">63,163,12</td>
                                    <td style="background:rgb(63,163,12);width: 100px;">
                                    </td>
                                    <td class="center">1558</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">211</td>
                                    <td>Thio Violet</td>
                                    <td class="spaced">94,10,28</td>
                                    <td style="background:rgb(94,10,28);width: 100px;">
                                    </td>
                                    <td class="center">1645</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">223</td>
                                    <td>Venetian Red</td>
                                    <td class="spaced">117,43,29</td>
                                    <td style="background:rgb(117,43,29);width: 100px;">
                                    </td>
                                    <td class="center">2583</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">244</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">185,126,30</td>
                                    <td style="background:rgb(185,126,30);width: 100px;">
                                    </td>
                                    <td class="center">1927</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">248</td>
                                    <td>Zinc White</td>
                                    <td class="spaced">251,245,224</td>
                                    <td style="background:rgb(251,245,224);width: 100px;">
                                    </td>
                                    <td class="center">2599</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">306</td>
                                    <td>Thalo Green YS</td>
                                    <td class="spaced">0,49,37</td>
                                    <td style="background:rgb(0,49,37);width: 100px;">
                                    </td>
                                    <td class="center">1639</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">307</td>
                                    <td>Ultramarine Blue Deep</td>
                                    <td class="spaced">15,19,36</td>
                                    <td style="background:rgb(15,19,36);width: 100px;">
                                    </td>
                                    <td class="center">1572</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">309</td>
                                    <td>Cobalt Turqouise</td>
                                    <td class="spaced">0,163,167</td>
                                    <td style="background:rgb(0,163,167);width: 100px;">
                                    </td>
                                    <td class="center">1893</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">21211</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">253,253,247</td>
                                    <td style="background:rgb(253,253,247);width: 100px;">
                                    </td>
                                    <td class="center">2330</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-9" data-toggle="collapse" data-target="#datapnl-9">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Grumbacher Pre-Tested Professional Oil</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-9" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Alizarin Crimson</td>
                                    <td class="spaced">70,21,28</td>
                                    <td style="background:rgb(70,21,28);width: 100px;">
                                    </td>
                                    <td class="center">1301</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">23</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">97,46,36</td>
                                    <td style="background:rgb(97,46,36);width: 100px;">
                                    </td>
                                    <td class="center">1755</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">24</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">47,37,31</td>
                                    <td style="background:rgb(47,37,31);width: 100px;">
                                    </td>
                                    <td class="center">1731</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">25</td>
                                    <td>Cadmium Orange Medium</td>
                                    <td class="spaced">225,98,0</td>
                                    <td style="background:rgb(225,98,0);width: 100px;">
                                    </td>
                                    <td class="center">2384</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">26</td>
                                    <td>Cadmium Red Deep</td>
                                    <td class="spaced">144,6,30</td>
                                    <td style="background:rgb(144,6,30);width: 100px;">
                                    </td>
                                    <td class="center">2387</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">27</td>
                                    <td>Cadmium Red Light</td>
                                    <td class="spaced">218,34,23</td>
                                    <td style="background:rgb(218,34,23);width: 100px;">
                                    </td>
                                    <td class="center">2795</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">29</td>
                                    <td>Cadmium Red Medium</td>
                                    <td class="spaced">169,6,30</td>
                                    <td style="background:rgb(169,6,30);width: 100px;">
                                    </td>
                                    <td class="center">2275</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">30</td>
                                    <td>Cadmium Red</td>
                                    <td class="spaced">196,25,36</td>
                                    <td style="background:rgb(196,25,36);width: 100px;">
                                    </td>
                                    <td class="center">2548</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">31</td>
                                    <td>Cadmium Yellow Deep</td>
                                    <td class="spaced">255,145,0</td>
                                    <td style="background:rgb(255,145,0);width: 100px;">
                                    </td>
                                    <td class="center">2451</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">33</td>
                                    <td>Cadmium Yellow Light</td>
                                    <td class="spaced">255,194,0</td>
                                    <td style="background:rgb(255,194,0);width: 100px;">
                                    </td>
                                    <td class="center">2340</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">34</td>
                                    <td>Cadmium Yellow Medium</td>
                                    <td class="spaced">255,163,0</td>
                                    <td style="background:rgb(255,163,0);width: 100px;">
                                    </td>
                                    <td class="center">2167</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">36</td>
                                    <td>Cadmium Yellow Pale</td>
                                    <td class="spaced">252,219,0</td>
                                    <td style="background:rgb(252,219,0);width: 100px;">
                                    </td>
                                    <td class="center">2739</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">40</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,80,113</td>
                                    <td style="background:rgb(0,80,113);width: 100px;">
                                    </td>
                                    <td class="center">2470</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">48</td>
                                    <td>Chromium Oxide Green</td>
                                    <td class="spaced">64,101,59</td>
                                    <td style="background:rgb(64,101,59);width: 100px;">
                                    </td>
                                    <td class="center">2958</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">49</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">22,51,110</td>
                                    <td style="background:rgb(22,51,110);width: 100px;">
                                    </td>
                                    <td class="center">2015</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">51</td>
                                    <td>Cobalt Rose</td>
                                    <td class="spaced">103,53,73</td>
                                    <td style="background:rgb(103,53,73);width: 100px;">
                                    </td>
                                    <td class="center">1658</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">60</td>
                                    <td>Diarylide Yellow</td>
                                    <td class="spaced">255,143,0</td>
                                    <td style="background:rgb(255,143,0);width: 100px;">
                                    </td>
                                    <td class="center">1380</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">61</td>
                                    <td>Dioxazine Purple</td>
                                    <td class="spaced">44,42,44</td>
                                    <td style="background:rgb(44,42,44);width: 100px;">
                                    </td>
                                    <td class="center">1620</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">76</td>
                                    <td>French Ultramarine Blue</td>
                                    <td class="spaced">16,16,38</td>
                                    <td style="background:rgb(16,16,38);width: 100px;">
                                    </td>
                                    <td class="center">1663</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">95</td>
                                    <td>Grumbacher Red</td>
                                    <td class="spaced">193,20,9</td>
                                    <td style="background:rgb(193,20,9);width: 100px;">
                                    </td>
                                    <td class="center">1683</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">102</td>
                                    <td>Hansa Yellow</td>
                                    <td class="spaced">244,190,0</td>
                                    <td style="background:rgb(244,190,0);width: 100px;">
                                    </td>
                                    <td class="center">1429</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">109</td>
                                    <td>Indanthrone Blue</td>
                                    <td class="spaced">26,20,28</td>
                                    <td style="background:rgb(26,20,28);width: 100px;">
                                    </td>
                                    <td class="center">1517</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">115</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">34,35,36</td>
                                    <td style="background:rgb(34,35,36);width: 100px;">
                                    </td>
                                    <td class="center">1733</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">160</td>
                                    <td>Permanent Blue</td>
                                    <td class="spaced">25,26,46</td>
                                    <td style="background:rgb(25,26,46);width: 100px;">
                                    </td>
                                    <td class="center">1763</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">166</td>
                                    <td>Prussian Green</td>
                                    <td class="spaced">43,70,25</td>
                                    <td style="background:rgb(43,70,25);width: 100px;">
                                    </td>
                                    <td class="center">1470</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">168</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">23,15,12</td>
                                    <td style="background:rgb(23,15,12);width: 100px;">
                                    </td>
                                    <td class="center">1430</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">170</td>
                                    <td>Quinacridone Red</td>
                                    <td class="spaced">158,11,37</td>
                                    <td style="background:rgb(158,11,37);width: 100px;">
                                    </td>
                                    <td class="center">1411</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">171</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">151,92,41</td>
                                    <td style="background:rgb(151,92,41);width: 100px;">
                                    </td>
                                    <td class="center">1988</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">172</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">52,45,38</td>
                                    <td style="background:rgb(52,45,38);width: 100px;">
                                    </td>
                                    <td class="center">1622</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">200</td>
                                    <td>Superba White</td>
                                    <td class="spaced">253,249,228</td>
                                    <td style="background:rgb(253,249,228);width: 100px;">
                                    </td>
                                    <td class="center">2724</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">203</td>
                                    <td>Thalo Blue</td>
                                    <td class="spaced">27,15,54</td>
                                    <td style="background:rgb(27,15,54);width: 100px;">
                                    </td>
                                    <td class="center">1333</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">205</td>
                                    <td>Thalo Green (Blue Shade)</td>
                                    <td class="spaced">0,28,36</td>
                                    <td style="background:rgb(0,28,36);width: 100px;">
                                    </td>
                                    <td class="center">1505</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">208</td>
                                    <td>Thalo Red Rose</td>
                                    <td class="spaced">132,16,32</td>
                                    <td style="background:rgb(132,16,32);width: 100px;">
                                    </td>
                                    <td class="center">1434</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">211</td>
                                    <td>Thio Violet</td>
                                    <td class="spaced">86,29,41</td>
                                    <td style="background:rgb(86,29,41);width: 100px;">
                                    </td>
                                    <td class="center">1473</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">218</td>
                                    <td>Unbleached Titanium White</td>
                                    <td class="spaced">191,173,141</td>
                                    <td style="background:rgb(191,173,141);width: 100px;">
                                    </td>
                                    <td class="center">2542</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">232</td>
                                    <td>Viridian</td>
                                    <td class="spaced">0,56,44</td>
                                    <td style="background:rgb(0,56,44);width: 100px;">
                                    </td>
                                    <td class="center">1639</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">244</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">181,124,41</td>
                                    <td style="background:rgb(181,124,41);width: 100px;">
                                    </td>
                                    <td class="center">1905</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">306</td>
                                    <td>Thalo&#xAE; Green Yellow Shade</td>
                                    <td class="spaced">0,44,39</td>
                                    <td style="background:rgb(0,44,39);width: 100px;">
                                    </td>
                                    <td class="center">1457</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">309</td>
                                    <td>Cobalt Turquoise</td>
                                    <td class="spaced">0,149,154</td>
                                    <td style="background:rgb(0,149,154);width: 100px;">
                                    </td>
                                    <td class="center">2146</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">310</td>
                                    <td>Cobalt Blue Deep</td>
                                    <td class="spaced">3,47,96</td>
                                    <td style="background:rgb(3,47,96);width: 100px;">
                                    </td>
                                    <td class="center">2085</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">311</td>
                                    <td>Bismuth Yellow</td>
                                    <td class="spaced">254,226,0</td>
                                    <td style="background:rgb(254,226,0);width: 100px;">
                                    </td>
                                    <td class="center">1828</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">312</td>
                                    <td>Pyrrole Red</td>
                                    <td class="spaced">210,25,24</td>
                                    <td style="background:rgb(210,25,24);width: 100px;">
                                    </td>
                                    <td class="center">1759</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">315</td>
                                    <td>Perylene Red</td>
                                    <td class="spaced">116,6,22</td>
                                    <td style="background:rgb(116,6,22);width: 100px;">
                                    </td>
                                    <td class="center">1653</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">21211</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">253,251,241</td>
                                    <td style="background:rgb(253,251,241);width: 100px;">
                                    </td>
                                    <td class="center">2662</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-10" data-toggle="collapse" data-target="#datapnl-10">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Liquitex Heavy Body Acrylic</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-10" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">118</td>
                                    <td>Quinacridone Blue Violet</td>
                                    <td class="spaced">46,18,30</td>
                                    <td style="background:rgb(46,18,30);width: 100px;">
                                    </td>
                                    <td class="center">892</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">127</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">115,64,57</td>
                                    <td style="background:rgb(115,64,57);width: 100px;">
                                    </td>
                                    <td class="center">1044</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">150</td>
                                    <td>Cadmium Orange</td>
                                    <td class="spaced">255,121,0</td>
                                    <td style="background:rgb(255,121,0);width: 100px;">
                                    </td>
                                    <td class="center">1129</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">152</td>
                                    <td>Cadmium Red Light</td>
                                    <td class="spaced">226,52,28</td>
                                    <td style="background:rgb(226,52,28);width: 100px;">
                                    </td>
                                    <td class="center">1098</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">163</td>
                                    <td>Cadmium Yellow Deep Hue</td>
                                    <td class="spaced">255,171,0</td>
                                    <td style="background:rgb(255,171,0);width: 100px;">
                                    </td>
                                    <td class="center">946</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">164</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,96,161</td>
                                    <td style="background:rgb(0,96,161);width: 100px;">
                                    </td>
                                    <td class="center">1084</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">172</td>
                                    <td>Cobalt Teal</td>
                                    <td class="spaced">0,169,177</td>
                                    <td style="background:rgb(0,169,177);width: 100px;">
                                    </td>
                                    <td class="center">1014</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">244</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">44,43,47</td>
                                    <td style="background:rgb(44,43,47);width: 100px;">
                                    </td>
                                    <td class="center">984</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">292</td>
                                    <td>Naphthol</td>
                                    <td class="spaced">171,0,32</td>
                                    <td style="background:rgb(171,0,32);width: 100px;">
                                    </td>
                                    <td class="center">902</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">300</td>
                                    <td>Deep Magenta</td>
                                    <td class="spaced">96,17,59</td>
                                    <td style="background:rgb(96,17,59);width: 100px;">
                                    </td>
                                    <td class="center">906</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">312</td>
                                    <td>Light Green Permanent</td>
                                    <td class="spaced">0,142,49</td>
                                    <td style="background:rgb(0,142,49);width: 100px;">
                                    </td>
                                    <td class="center">923</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">316</td>
                                    <td>Phthalocyanine Blue GS</td>
                                    <td class="spaced">33,25,64</td>
                                    <td style="background:rgb(33,25,64);width: 100px;">
                                    </td>
                                    <td class="center">955</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">319</td>
                                    <td>Phthalocyanine Green YS</td>
                                    <td class="spaced">0,45,42</td>
                                    <td style="background:rgb(0,45,42);width: 100px;">
                                    </td>
                                    <td class="center">917</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">330</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">150,92,57</td>
                                    <td style="background:rgb(150,92,57);width: 100px;">
                                    </td>
                                    <td class="center">1046</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">381</td>
                                    <td>Cobalt Blue Hue</td>
                                    <td class="spaced">49,58,151</td>
                                    <td style="background:rgb(49,58,151);width: 100px;">
                                    </td>
                                    <td class="center">1039</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">432</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">255,249,255</td>
                                    <td style="background:rgb(255,249,255);width: 100px;">
                                    </td>
                                    <td class="center">1156</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">500</td>
                                    <td>Medium Magenta</td>
                                    <td class="spaced">190,67,152</td>
                                    <td style="background:rgb(190,67,152);width: 100px;">
                                    </td>
                                    <td class="center">983</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">599</td>
                                    <td>Neutral Gray Val.5</td>
                                    <td class="spaced">121,119,125</td>
                                    <td style="background:rgb(121,119,125);width: 100px;">
                                    </td>
                                    <td class="center">1057</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">650</td>
                                    <td>Light Emerald Green</td>
                                    <td class="spaced">68,169,74</td>
                                    <td style="background:rgb(68,169,74);width: 100px;">
                                    </td>
                                    <td class="center">996</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">740</td>
                                    <td>Vivid Lime Green</td>
                                    <td class="spaced">131,189,58</td>
                                    <td style="background:rgb(131,189,58);width: 100px;">
                                    </td>
                                    <td class="center">914</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">770</td>
                                    <td>Light Blue Permanent</td>
                                    <td class="spaced">61,186,221</td>
                                    <td style="background:rgb(61,186,221);width: 100px;">
                                    </td>
                                    <td class="center">1068</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">830</td>
                                    <td>Cadmium Yellow Med. Hue</td>
                                    <td class="spaced">255,190,0</td>
                                    <td style="background:rgb(255,190,0);width: 100px;">
                                    </td>
                                    <td class="center">917</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-11" data-toggle="collapse" data-target="#datapnl-11">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Polycolor - Maimeri</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-11" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">18</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">253,254,249</td>
                                    <td style="background:rgb(253,254,249);width: 100px;">
                                    </td>
                                    <td class="center">1669</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">52</td>
                                    <td>Brilliant Orange</td>
                                    <td class="spaced">216,77,44</td>
                                    <td style="background:rgb(216,77,44);width: 100px;">
                                    </td>
                                    <td class="center">1553</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">74</td>
                                    <td>Brilliant Yellow Light</td>
                                    <td class="spaced">255,245,135</td>
                                    <td style="background:rgb(255,245,135);width: 100px;">
                                    </td>
                                    <td class="center">1654</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">100</td>
                                    <td>Lemon Yellow</td>
                                    <td class="spaced">239,217,0</td>
                                    <td style="background:rgb(239,217,0);width: 100px;">
                                    </td>
                                    <td class="center">1599</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">116</td>
                                    <td>Primary Yellow</td>
                                    <td class="spaced">255,217,0</td>
                                    <td style="background:rgb(255,217,0);width: 100px;">
                                    </td>
                                    <td class="center">1658</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">118</td>
                                    <td>Deep Yellow</td>
                                    <td class="spaced">255,263,0</td>
                                    <td style="background:rgb(255,263,0);width: 100px;">
                                    </td>
                                    <td class="center">1592</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">131</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">203,148,72</td>
                                    <td style="background:rgb(203,148,72);width: 100px;">
                                    </td>
                                    <td class="center">1636</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">161</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">179,114,67</td>
                                    <td style="background:rgb(179,114,67);width: 100px;">
                                    </td>
                                    <td class="center">1692</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">166</td>
                                    <td>Carmine</td>
                                    <td class="spaced">154,52,53</td>
                                    <td style="background:rgb(154,52,53);width: 100px;">
                                    </td>
                                    <td class="center">1633</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">191</td>
                                    <td>Red Ochre</td>
                                    <td class="spaced">139,69,55</td>
                                    <td style="background:rgb(139,69,55);width: 100px;">
                                    </td>
                                    <td class="center">1782</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">220</td>
                                    <td>Briliant Red</td>
                                    <td class="spaced">202,62,44</td>
                                    <td style="background:rgb(202,62,44);width: 100px;">
                                    </td>
                                    <td class="center">1670</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">256</td>
                                    <td>Primary Red - Magenta</td>
                                    <td class="spaced">130,47,71</td>
                                    <td style="background:rgb(130,47,71);width: 100px;">
                                    </td>
                                    <td class="center">1512</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">278</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">121,76,64</td>
                                    <td style="background:rgb(121,76,64);width: 100px;">
                                    </td>
                                    <td class="center">1838</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">280</td>
                                    <td>Vermilion Hue</td>
                                    <td class="spaced">195,53,48</td>
                                    <td style="background:rgb(195,53,48);width: 100px;">
                                    </td>
                                    <td class="center">1509</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">304</td>
                                    <td>Brilliant Green Light</td>
                                    <td class="spaced">0,161,90</td>
                                    <td style="background:rgb(0,161,90);width: 100px;">
                                    </td>
                                    <td class="center">1626</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">305</td>
                                    <td>Brilliant Green Deep</td>
                                    <td class="spaced">0,111,69</td>
                                    <td style="background:rgb(0,111,69);width: 100px;">
                                    </td>
                                    <td class="center">1571</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">321</td>
                                    <td>Phthalo Green</td>
                                    <td class="spaced">28,73,71</td>
                                    <td style="background:rgb(28,73,71);width: 100px;">
                                    </td>
                                    <td class="center">1394</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">323</td>
                                    <td>Yellowish Green</td>
                                    <td class="spaced">120,210,91</td>
                                    <td style="background:rgb(120,210,91);width: 100px;">
                                    </td>
                                    <td class="center">1601</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">356</td>
                                    <td>Emerald Green</td>
                                    <td class="spaced">0,132,118</td>
                                    <td style="background:rgb(0,132,118);width: 100px;">
                                    </td>
                                    <td class="center">1624</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">358</td>
                                    <td>Sap Green</td>
                                    <td class="spaced">55,62,57</td>
                                    <td style="background:rgb(55,62,57);width: 100px;">
                                    </td>
                                    <td class="center">1545</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">366</td>
                                    <td>Sky Blue Celeste</td>
                                    <td class="spaced">0,123,185</td>
                                    <td style="background:rgb(0,123,185);width: 100px;">
                                    </td>
                                    <td class="center">1743</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">378</td>
                                    <td>Phthalo Blue</td>
                                    <td class="spaced">28,101,164</td>
                                    <td style="background:rgb(28,101,164);width: 100px;">
                                    </td>
                                    <td class="center">1665</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">390</td>
                                    <td>Ultramarine</td>
                                    <td class="spaced">40,44,138</td>
                                    <td style="background:rgb(40,44,138);width: 100px;">
                                    </td>
                                    <td class="center">1618</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">400</td>
                                    <td>Primary Blue - Cyan</td>
                                    <td class="spaced">0,107,146</td>
                                    <td style="background:rgb(0,107,146);width: 100px;">
                                    </td>
                                    <td class="center">1615</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">404</td>
                                    <td>King&#xB4;s Blue</td>
                                    <td class="spaced">34,177,211</td>
                                    <td style="background:rgb(34,177,211);width: 100px;">
                                    </td>
                                    <td class="center">1678</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">408</td>
                                    <td>Turqouise Blue</td>
                                    <td class="spaced">0,118,122</td>
                                    <td style="background:rgb(0,118,122);width: 100px;">
                                    </td>
                                    <td class="center">1590</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">438</td>
                                    <td>Lilac</td>
                                    <td class="spaced">172,150,199</td>
                                    <td style="background:rgb(172,150,199);width: 100px;">
                                    </td>
                                    <td class="center">1589</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">443</td>
                                    <td>Violet</td>
                                    <td class="spaced">62,54,67</td>
                                    <td style="background:rgb(62,54,67);width: 100px;">
                                    </td>
                                    <td class="center">1559</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">447</td>
                                    <td>Brilliant Violet</td>
                                    <td class="spaced">119,94,171</td>
                                    <td style="background:rgb(119,94,171);width: 100px;">
                                    </td>
                                    <td class="center">1640</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">492</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">82,62,57</td>
                                    <td style="background:rgb(82,62,57);width: 100px;">
                                    </td>
                                    <td class="center">1672</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">493</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">88,72,61</td>
                                    <td style="background:rgb(88,72,61);width: 100px;">
                                    </td>
                                    <td class="center">1917</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">530</td>
                                    <td>Black</td>
                                    <td class="spaced">35,35,35</td>
                                    <td style="background:rgb(35,35,35);width: 100px;">
                                    </td>
                                    <td class="center">1363</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-12" data-toggle="collapse" data-target="#datapnl-12">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Primacryl - Schmincke</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-12" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">101</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">254,254,251</td>
                                    <td style="background:rgb(254,254,251);width: 100px;">
                                    </td>
                                    <td class="center">1768</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">205</td>
                                    <td>Lemon Yellow</td>
                                    <td class="spaced">248,224,0</td>
                                    <td style="background:rgb(248,224,0);width: 100px;">
                                    </td>
                                    <td class="center">1356</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">207</td>
                                    <td>Cadmium Yellow Light</td>
                                    <td class="spaced">255,227,0</td>
                                    <td style="background:rgb(255,227,0);width: 100px;">
                                    </td>
                                    <td class="center">1411</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">211</td>
                                    <td>Cadmium Yellow Medium</td>
                                    <td class="spaced">255,206,0</td>
                                    <td style="background:rgb(255,206,0);width: 100px;">
                                    </td>
                                    <td class="center">1551</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">213</td>
                                    <td>Cadmium Yellow Deep</td>
                                    <td class="spaced">255,159,0</td>
                                    <td style="background:rgb(255,159,0);width: 100px;">
                                    </td>
                                    <td class="center">1522</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">215</td>
                                    <td>Brilliant Orange</td>
                                    <td class="spaced">242,73,0</td>
                                    <td style="background:rgb(242,73,0);width: 100px;">
                                    </td>
                                    <td class="center">1396</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">317</td>
                                    <td>Cadmium Red Light</td>
                                    <td class="spaced">229,42,14</td>
                                    <td style="background:rgb(229,42,14);width: 100px;">
                                    </td>
                                    <td class="center">1528</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">320</td>
                                    <td>Cadmium Red Medium</td>
                                    <td class="spaced">197,0,27</td>
                                    <td style="background:rgb(197,0,27);width: 100px;">
                                    </td>
                                    <td class="center">1566</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">321</td>
                                    <td>Carmine</td>
                                    <td class="spaced">182,0,16</td>
                                    <td style="background:rgb(182,0,16);width: 100px;">
                                    </td>
                                    <td class="center">1234</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">322</td>
                                    <td>Cadmium Red Deep</td>
                                    <td class="spaced">173,3,35</td>
                                    <td style="background:rgb(173,3,35);width: 100px;">
                                    </td>
                                    <td class="center">1591</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">325</td>
                                    <td>Quinacridone Red</td>
                                    <td class="spaced">146,0,34</td>
                                    <td style="background:rgb(146,0,34);width: 100px;">
                                    </td>
                                    <td class="center">1308</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">326</td>
                                    <td>Quinacridone Magenta</td>
                                    <td class="spaced">157,25,78</td>
                                    <td style="background:rgb(157,25,78);width: 100px;">
                                    </td>
                                    <td class="center">1282</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">327</td>
                                    <td>Magenta</td>
                                    <td class="spaced">197,87,153</td>
                                    <td style="background:rgb(197,87,153);width: 100px;">
                                    </td>
                                    <td class="center">1464</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">328</td>
                                    <td>Quinacridone Violet</td>
                                    <td class="spaced">110,0,42</td>
                                    <td style="background:rgb(110,0,42);width: 100px;">
                                    </td>
                                    <td class="center">1307</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">433</td>
                                    <td>Ultramarine Blue</td>
                                    <td class="spaced">50,47,78</td>
                                    <td style="background:rgb(50,47,78);width: 100px;">
                                    </td>
                                    <td class="center">1437</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">434</td>
                                    <td>Cobalt Blue Deep</td>
                                    <td class="spaced">45,69,124</td>
                                    <td style="background:rgb(45,69,124);width: 100px;">
                                    </td>
                                    <td class="center">1463</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">435</td>
                                    <td>Cobalt Blue Light</td>
                                    <td class="spaced">36,94,190</td>
                                    <td style="background:rgb(36,94,190);width: 100px;">
                                    </td>
                                    <td class="center">1432</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">438</td>
                                    <td>Phthalo Blue rs</td>
                                    <td class="spaced">29,44,87</td>
                                    <td style="background:rgb(29,44,87);width: 100px;">
                                    </td>
                                    <td class="center">1311</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">439</td>
                                    <td>Phthalo Blue Cyan</td>
                                    <td class="spaced">0,53,107</td>
                                    <td style="background:rgb(0,53,107);width: 100px;">
                                    </td>
                                    <td class="center">1377</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">440</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">47,60,70</td>
                                    <td style="background:rgb(47,60,70);width: 100px;">
                                    </td>
                                    <td class="center">1378</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">454</td>
                                    <td>Cerulean blue</td>
                                    <td class="spaced">0,122,163</td>
                                    <td style="background:rgb(0,122,163);width: 100px;">
                                    </td>
                                    <td class="center">1410</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">561</td>
                                    <td>Turmaline Green</td>
                                    <td class="spaced">0,80,61</td>
                                    <td style="background:rgb(0,80,61);width: 100px;">
                                    </td>
                                    <td class="center">1560</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">562</td>
                                    <td>Chromium Oxide Green Brilliant</td>
                                    <td class="spaced">0,78,67</td>
                                    <td style="background:rgb(0,78,67);width: 100px;">
                                    </td>
                                    <td class="center">1362</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">563</td>
                                    <td>Phthalo Green bs</td>
                                    <td class="spaced">25,52,51</td>
                                    <td style="background:rgb(25,52,51);width: 100px;">
                                    </td>
                                    <td class="center">1297</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">564</td>
                                    <td>Phthalo Green ys</td>
                                    <td class="spaced">0,76,47</td>
                                    <td style="background:rgb(0,76,47);width: 100px;">
                                    </td>
                                    <td class="center">1341</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">567</td>
                                    <td>Permanent Green Light</td>
                                    <td class="spaced">54,165,73</td>
                                    <td style="background:rgb(54,165,73);width: 100px;">
                                    </td>
                                    <td class="center">1456</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">675</td>
                                    <td>Light Ochre</td>
                                    <td class="spaced">171,111,23</td>
                                    <td style="background:rgb(171,111,23);width: 100px;">
                                    </td>
                                    <td class="center">1375</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">677</td>
                                    <td>Raw umber</td>
                                    <td class="spaced">106,76,42</td>
                                    <td style="background:rgb(106,76,42);width: 100px;">
                                    </td>
                                    <td class="center">1404</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">678</td>
                                    <td>Sienna</td>
                                    <td class="spaced">134,83,39</td>
                                    <td style="background:rgb(134,83,39);width: 100px;">
                                    </td>
                                    <td class="center">1391</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">679</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">117,45,25</td>
                                    <td style="background:rgb(117,45,25);width: 100px;">
                                    </td>
                                    <td class="center">1436</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">684</td>
                                    <td>Natural Burnt Umber</td>
                                    <td class="spaced">70,49,41</td>
                                    <td style="background:rgb(70,49,41);width: 100px;">
                                    </td>
                                    <td class="center">1492</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">792</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">35,35,35</td>
                                    <td style="background:rgb(35,35,35);width: 100px;">
                                    </td>
                                    <td class="center">1221</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-13" data-toggle="collapse" data-target="#datapnl-13">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Professional Acrylic - Winsor &amp; Newton</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-13" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">19</td>
                                    <td>Azo Yellow Medium</td>
                                    <td class="spaced">255,206,0</td>
                                    <td style="background:rgb(255,206,0);width: 100px;">
                                    </td>
                                    <td class="center">1321</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">25</td>
                                    <td>Bismuth Yellow</td>
                                    <td class="spaced">255,235,0</td>
                                    <td style="background:rgb(255,235,0);width: 100px;">
                                    </td>
                                    <td class="center">1369</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">39</td>
                                    <td>Azo Yellow Deep</td>
                                    <td class="spaced">255,155,0</td>
                                    <td style="background:rgb(255,155,0);width: 100px;">
                                    </td>
                                    <td class="center">1330</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">60</td>
                                    <td>Buff Titanium</td>
                                    <td class="spaced">222,186,123</td>
                                    <td style="background:rgb(222,186,123);width: 100px;">
                                    </td>
                                    <td class="center">1578</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">74</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">81,36,24</td>
                                    <td style="background:rgb(81,36,24);width: 100px;">
                                    </td>
                                    <td class="center">1287</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">76</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">84,50,29</td>
                                    <td style="background:rgb(84,50,29);width: 100px;">
                                    </td>
                                    <td class="center">1369</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">86</td>
                                    <td>Cadmium Lemon</td>
                                    <td class="spaced">255,238,18</td>
                                    <td style="background:rgb(255,238,18);width: 100px;">
                                    </td>
                                    <td class="center">1538</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">89</td>
                                    <td>Cadmium Orange</td>
                                    <td class="spaced">255,122,0</td>
                                    <td style="background:rgb(255,122,0);width: 100px;">
                                    </td>
                                    <td class="center">1581</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">97</td>
                                    <td>Cadmium Red Deep</td>
                                    <td class="spaced">170,20,40</td>
                                    <td style="background:rgb(170,20,40);width: 100px;">
                                    </td>
                                    <td class="center">1413</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">99</td>
                                    <td>CadRedMed</td>
                                    <td class="spaced">106,37,39</td>
                                    <td style="background:rgb(106,37,39);width: 100px;">
                                    </td>
                                    <td class="center">1587</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">100</td>
                                    <td>Cadmium Red Light</td>
                                    <td class="spaced">230,55,20</td>
                                    <td style="background:rgb(230,55,20);width: 100px;">
                                    </td>
                                    <td class="center">1545</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">111</td>
                                    <td>Cadmium Yellow Deep</td>
                                    <td class="spaced">255,181,0</td>
                                    <td style="background:rgb(255,181,0);width: 100px;">
                                    </td>
                                    <td class="center">1493</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">116</td>
                                    <td>Cadmium Yellow Medium</td>
                                    <td class="spaced">255,201,0</td>
                                    <td style="background:rgb(255,201,0);width: 100px;">
                                    </td>
                                    <td class="center">1493</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">130</td>
                                    <td>Cerulean Blue Chromium</td>
                                    <td class="spaced">0,90,151</td>
                                    <td style="background:rgb(0,90,151);width: 100px;">
                                    </td>
                                    <td class="center">1477</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">137</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,108,163</td>
                                    <td style="background:rgb(0,108,163);width: 100px;">
                                    </td>
                                    <td class="center">1606</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">162</td>
                                    <td>Chromium Oxide Green</td>
                                    <td class="spaced">76,115,71</td>
                                    <td style="background:rgb(76,115,71);width: 100px;">
                                    </td>
                                    <td class="center">1682</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">178</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">22,71,153</td>
                                    <td style="background:rgb(22,71,153);width: 100px;">
                                    </td>
                                    <td class="center">1580</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">180</td>
                                    <td>Cobalt Blue Deep</td>
                                    <td class="spaced">57,50,125</td>
                                    <td style="background:rgb(57,50,125);width: 100px;">
                                    </td>
                                    <td class="center">1693</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">184</td>
                                    <td>Cobalt Green</td>
                                    <td class="spaced">0,131,107</td>
                                    <td style="background:rgb(0,131,107);width: 100px;">
                                    </td>
                                    <td class="center">1524</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">185</td>
                                    <td>Cobalt Green Deep</td>
                                    <td class="spaced">8,82,67</td>
                                    <td style="background:rgb(8,82,67);width: 100px;">
                                    </td>
                                    <td class="center">1554</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">191</td>
                                    <td>Cobalt Turquoise Light</td>
                                    <td class="spaced">0,163,166</td>
                                    <td style="background:rgb(0,163,166);width: 100px;">
                                    </td>
                                    <td class="center">1520</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">217</td>
                                    <td>Davy&#x27;s Gray</td>
                                    <td class="spaced">108,101,77</td>
                                    <td style="background:rgb(108,101,77);width: 100px;">
                                    </td>
                                    <td class="center">1448</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">229</td>
                                    <td>Dioxazine Purple</td>
                                    <td class="spaced">35,29,31</td>
                                    <td style="background:rgb(35,29,31);width: 100px;">
                                    </td>
                                    <td class="center">1213</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">294</td>
                                    <td>Green Gold</td>
                                    <td class="spaced">67,72,44</td>
                                    <td style="background:rgb(67,72,44);width: 100px;">
                                    </td>
                                    <td class="center">1295</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">311</td>
                                    <td>Hooker&#x27;s Green</td>
                                    <td class="spaced">52,64,38</td>
                                    <td style="background:rgb(52,64,38);width: 100px;">
                                    </td>
                                    <td class="center">1279</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">321</td>
                                    <td>Indanthrene Blue</td>
                                    <td class="spaced">34,21,36</td>
                                    <td style="background:rgb(34,21,36);width: 100px;">
                                    </td>
                                    <td class="center">1263</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">331</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">41,41,41</td>
                                    <td style="background:rgb(41,41,41);width: 100px;">
                                    </td>
                                    <td class="center">1359</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">346</td>
                                    <td>Lemon Yellow</td>
                                    <td class="spaced">243,224,0</td>
                                    <td style="background:rgb(243,224,0);width: 100px;">
                                    </td>
                                    <td class="center">1233</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">362</td>
                                    <td>Light Red</td>
                                    <td class="spaced">158,75,53</td>
                                    <td style="background:rgb(158,75,53);width: 100px;">
                                    </td>
                                    <td class="center">1421</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">386</td>
                                    <td>Mars Black</td>
                                    <td class="spaced">46,45,44</td>
                                    <td style="background:rgb(46,45,44);width: 100px;">
                                    </td>
                                    <td class="center">1550</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">421</td>
                                    <td>Naphthol Red Light</td>
                                    <td class="spaced">188,14,3</td>
                                    <td style="background:rgb(188,14,3);width: 100px;">
                                    </td>
                                    <td class="center">1236</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">423</td>
                                    <td>Naphthol Red Medium</td>
                                    <td class="spaced">175,0,7</td>
                                    <td style="background:rgb(175,0,7);width: 100px;">
                                    </td>
                                    <td class="center">1235</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">425</td>
                                    <td>Naples Yellow Deep</td>
                                    <td class="spaced">235,165,63</td>
                                    <td style="background:rgb(235,165,63);width: 100px;">
                                    </td>
                                    <td class="center">1491</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">439</td>
                                    <td>Nickel Azo Yellow</td>
                                    <td class="spaced">131,92,2</td>
                                    <td style="background:rgb(131,92,2);width: 100px;">
                                    </td>
                                    <td class="center">1312</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">447</td>
                                    <td>Olive Green</td>
                                    <td class="spaced">41,50,34</td>
                                    <td style="background:rgb(41,50,34);width: 100px;">
                                    </td>
                                    <td class="center">1263</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">460</td>
                                    <td>Perylene Green</td>
                                    <td class="spaced">39,32,32</td>
                                    <td style="background:rgb(39,32,32);width: 100px;">
                                    </td>
                                    <td class="center">1265</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">464</td>
                                    <td>Perylene Red</td>
                                    <td class="spaced">139,0,20</td>
                                    <td style="background:rgb(139,0,20);width: 100px;">
                                    </td>
                                    <td class="center">1289</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">466</td>
                                    <td>Permanent Alizarin Crimson</td>
                                    <td class="spaced">89,26,34</td>
                                    <td style="background:rgb(89,26,34);width: 100px;">
                                    </td>
                                    <td class="center">1191</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">470</td>
                                    <td>Perylene Violet</td>
                                    <td class="spaced">58,22,23</td>
                                    <td style="background:rgb(58,22,23);width: 100px;">
                                    </td>
                                    <td class="center">1239</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">503</td>
                                    <td>Permanent Sap Green</td>
                                    <td class="spaced">24,38,21</td>
                                    <td style="background:rgb(24,38,21);width: 100px;">
                                    </td>
                                    <td class="center">1289</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">507</td>
                                    <td>Perylene Maroon</td>
                                    <td class="spaced">76,20,22</td>
                                    <td style="background:rgb(76,20,22);width: 100px;">
                                    </td>
                                    <td class="center">1225</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">514</td>
                                    <td>Phthalo Blue (Red Shade)</td>
                                    <td class="spaced">25,14,58</td>
                                    <td style="background:rgb(25,14,58);width: 100px;">
                                    </td>
                                    <td class="center">1097</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">515</td>
                                    <td>Phthalo Blue (Green Shade)</td>
                                    <td class="spaced">16,36,53</td>
                                    <td style="background:rgb(16,36,53);width: 100px;">
                                    </td>
                                    <td class="center">1268</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">519</td>
                                    <td>Pyrrole Orange</td>
                                    <td class="spaced">244,66,0</td>
                                    <td style="background:rgb(244,66,0);width: 100px;">
                                    </td>
                                    <td class="center">1246</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">521</td>
                                    <td>Phthalo Green (Yellow Shade)</td>
                                    <td class="spaced">0,47,42</td>
                                    <td style="background:rgb(0,47,42);width: 100px;">
                                    </td>
                                    <td class="center">1286</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">522</td>
                                    <td>Phthalo Green (Blue Shade)</td>
                                    <td class="spaced">2,33,39</td>
                                    <td style="background:rgb(2,33,39);width: 100px;">
                                    </td>
                                    <td class="center">1289</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">526</td>
                                    <td>Phthalo Turquoise</td>
                                    <td class="spaced">0,55,60</td>
                                    <td style="background:rgb(0,55,60);width: 100px;">
                                    </td>
                                    <td class="center">1253</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">534</td>
                                    <td>Pyrrole Red</td>
                                    <td class="spaced">193,0,28</td>
                                    <td style="background:rgb(193,0,28);width: 100px;">
                                    </td>
                                    <td class="center">1252</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">536</td>
                                    <td>Pyrrole Red Light</td>
                                    <td class="spaced">215,34,34</td>
                                    <td style="background:rgb(215,34,34);width: 100px;">
                                    </td>
                                    <td class="center">1241</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">537</td>
                                    <td>Potter&#x27;s Pink</td>
                                    <td class="spaced">129,67,78</td>
                                    <td style="background:rgb(129,67,78);width: 100px;">
                                    </td>
                                    <td class="center">1380</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">545</td>
                                    <td>Quinacridone Magenta</td>
                                    <td class="spaced">78,17,31</td>
                                    <td style="background:rgb(78,17,31);width: 100px;">
                                    </td>
                                    <td class="center">1260</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">548</td>
                                    <td>Quinacridone Red</td>
                                    <td class="spaced">154,21,36</td>
                                    <td style="background:rgb(154,21,36);width: 100px;">
                                    </td>
                                    <td class="center">1302</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">549</td>
                                    <td>Quinacridone Burnt Orange</td>
                                    <td class="spaced">74,36,35</td>
                                    <td style="background:rgb(74,36,35);width: 100px;">
                                    </td>
                                    <td class="center">1268</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">550</td>
                                    <td>Quinacridone Violet</td>
                                    <td class="spaced">96,22,47</td>
                                    <td style="background:rgb(96,22,47);width: 100px;">
                                    </td>
                                    <td class="center">1274</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">552</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">111,69,28</td>
                                    <td style="background:rgb(111,69,28);width: 100px;">
                                    </td>
                                    <td class="center">1346</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">554</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">62,54,46</td>
                                    <td style="background:rgb(62,54,46);width: 100px;">
                                    </td>
                                    <td class="center">1329</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">644</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">253,254,249</td>
                                    <td style="background:rgb(253,254,249);width: 100px;">
                                    </td>
                                    <td class="center">1728</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">664</td>
                                    <td>Ultramarine Blue</td>
                                    <td class="spaced">53,48,83</td>
                                    <td style="background:rgb(53,48,83);width: 100px;">
                                    </td>
                                    <td class="center">1385</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">672</td>
                                    <td>Ultramarine Violet</td>
                                    <td class="spaced">54,52,68</td>
                                    <td style="background:rgb(54,52,68);width: 100px;">
                                    </td>
                                    <td class="center">1435</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">744</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">162,109,51</td>
                                    <td style="background:rgb(162,109,51);width: 100px;">
                                    </td>
                                    <td class="center">1436</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-14" data-toggle="collapse" data-target="#datapnl-14">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Rembrandt Extra-Fine Artists&#x27; Oil</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-14" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">105</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">253,254,249</td>
                                    <td style="background:rgb(253,254,249);width: 100px;">
                                    </td>
                                    <td class="center">2333</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">207</td>
                                    <td>Cadm. Yellow Lemon</td>
                                    <td class="spaced">248,222,2</td>
                                    <td style="background:rgb(248,222,2);width: 100px;">
                                    </td>
                                    <td class="center">2524</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">211</td>
                                    <td>Cadmium Orange</td>
                                    <td class="spaced">255,110,14</td>
                                    <td style="background:rgb(255,110,14);width: 100px;">
                                    </td>
                                    <td class="center">2552</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">227</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">172,119,38</td>
                                    <td style="background:rgb(172,119,38);width: 100px;">
                                    </td>
                                    <td class="center">2056</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">232</td>
                                    <td>Orange Ochre</td>
                                    <td class="spaced">147,76,44</td>
                                    <td style="background:rgb(147,76,44);width: 100px;">
                                    </td>
                                    <td class="center">2078</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">234</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">139,95,47</td>
                                    <td style="background:rgb(139,95,47);width: 100px;">
                                    </td>
                                    <td class="center">1789</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">271</td>
                                    <td>Cadmium Yellow M</td>
                                    <td class="spaced">255,192,0</td>
                                    <td style="background:rgb(255,192,0);width: 100px;">
                                    </td>
                                    <td class="center">2513</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">303</td>
                                    <td>Cadmium Red L</td>
                                    <td class="spaced">231,56,8</td>
                                    <td style="background:rgb(231,56,8);width: 100px;">
                                    </td>
                                    <td class="center">2489</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">306</td>
                                    <td>Cadmium Red D</td>
                                    <td class="spaced">182,21,35</td>
                                    <td style="background:rgb(182,21,35);width: 100px;">
                                    </td>
                                    <td class="center">2592</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">311</td>
                                    <td>Vermilion</td>
                                    <td class="spaced">245,69,0</td>
                                    <td style="background:rgb(245,69,0);width: 100px;">
                                    </td>
                                    <td class="center">1732</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">314</td>
                                    <td>Cadmium Red M</td>
                                    <td class="spaced">205,38,30</td>
                                    <td style="background:rgb(205,38,30);width: 100px;">
                                    </td>
                                    <td class="center">2812</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">318</td>
                                    <td>Carmine</td>
                                    <td class="spaced">112,17,28</td>
                                    <td style="background:rgb(112,17,28);width: 100px;">
                                    </td>
                                    <td class="center">1754</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">334</td>
                                    <td>Scarlet </td>
                                    <td class="spaced">143,16,35</td>
                                    <td style="background:rgb(143,16,35);width: 100px;">
                                    </td>
                                    <td class="center">1637</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">342</td>
                                    <td>Perm.Madder D</td>
                                    <td class="spaced">99,30,43</td>
                                    <td style="background:rgb(99,30,43);width: 100px;">
                                    </td>
                                    <td class="center">1598</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">349</td>
                                    <td>Venetian Red </td>
                                    <td class="spaced">120,48,38</td>
                                    <td style="background:rgb(120,48,38);width: 100px;">
                                    </td>
                                    <td class="center">2517</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">366</td>
                                    <td>Quinacridone Rose</td>
                                    <td class="spaced">127,26,42</td>
                                    <td style="background:rgb(127,26,42);width: 100px;">
                                    </td>
                                    <td class="center">1612</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">408</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">50,43,38</td>
                                    <td style="background:rgb(50,43,38);width: 100px;">
                                    </td>
                                    <td class="center">1722</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">409</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">60,40,35</td>
                                    <td style="background:rgb(60,40,35);width: 100px;">
                                    </td>
                                    <td class="center">1694</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">411</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">101,56,47</td>
                                    <td style="background:rgb(101,56,47);width: 100px;">
                                    </td>
                                    <td class="center">1898</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">506</td>
                                    <td>Ultramarine D</td>
                                    <td class="spaced">30,29,160</td>
                                    <td style="background:rgb(30,29,160);width: 100px;">
                                    </td>
                                    <td class="center">1884</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">507</td>
                                    <td>Ultramarine Violet</td>
                                    <td class="spaced">78,67,149</td>
                                    <td style="background:rgb(78,67,149);width: 100px;">
                                    </td>
                                    <td class="center">1898</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">508</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">24,28,43</td>
                                    <td style="background:rgb(24,28,43);width: 100px;">
                                    </td>
                                    <td class="center">1706</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">515</td>
                                    <td>Cobalt Blue D</td>
                                    <td class="spaced">24,40,100</td>
                                    <td style="background:rgb(24,40,100);width: 100px;">
                                    </td>
                                    <td class="center">2198</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">534</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,121,194</td>
                                    <td style="background:rgb(0,121,194);width: 100px;">
                                    </td>
                                    <td class="center">2369</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">537</td>
                                    <td>Perm.Violet M</td>
                                    <td class="spaced">99,0,54</td>
                                    <td style="background:rgb(99,0,54);width: 100px;">
                                    </td>
                                    <td class="center">1475</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">539</td>
                                    <td>Cobalt Violet</td>
                                    <td class="spaced">132,61,111</td>
                                    <td style="background:rgb(132,61,111);width: 100px;">
                                    </td>
                                    <td class="center">1978</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">568</td>
                                    <td>Perm. Blue Violet</td>
                                    <td class="spaced">87,24,114</td>
                                    <td style="background:rgb(87,24,114);width: 100px;">
                                    </td>
                                    <td class="center">1947</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">576</td>
                                    <td>Phthalo BlueGreen </td>
                                    <td class="spaced">29,22,56</td>
                                    <td style="background:rgb(29,22,56);width: 100px;">
                                    </td>
                                    <td class="center">1618</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">583</td>
                                    <td>Phthalo Blue Red</td>
                                    <td class="spaced">7,43,115</td>
                                    <td style="background:rgb(7,43,115);width: 100px;">
                                    </td>
                                    <td class="center">1636</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">585</td>
                                    <td>Indanthrene Blue</td>
                                    <td class="spaced">30,32,47</td>
                                    <td style="background:rgb(30,32,47);width: 100px;">
                                    </td>
                                    <td class="center">1544</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">586</td>
                                    <td>Cobalt Turq.Blue</td>
                                    <td class="spaced">0,96,126</td>
                                    <td style="background:rgb(0,96,126);width: 100px;">
                                    </td>
                                    <td class="center">2342</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">610</td>
                                    <td>Cobalt Green</td>
                                    <td class="spaced">0,104,90</td>
                                    <td style="background:rgb(0,104,90);width: 100px;">
                                    </td>
                                    <td class="center">2393</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">616</td>
                                    <td>Viridian</td>
                                    <td class="spaced">0,89,85</td>
                                    <td style="background:rgb(0,89,85);width: 100px;">
                                    </td>
                                    <td class="center">1757</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">623</td>
                                    <td>Sap Green</td>
                                    <td class="spaced">73,99,61</td>
                                    <td style="background:rgb(73,99,61);width: 100px;">
                                    </td>
                                    <td class="center">1859</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">668</td>
                                    <td>Chromium Ox.Green</td>
                                    <td class="spaced">69,106,66</td>
                                    <td style="background:rgb(69,106,66);width: 100px;">
                                    </td>
                                    <td class="center">2465</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">680</td>
                                    <td>Phthalo GreenBlue</td>
                                    <td class="spaced">0,67,52</td>
                                    <td style="background:rgb(0,67,52);width: 100px;">
                                    </td>
                                    <td class="center">1758</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">681</td>
                                    <td>Phthalo Green Yellow</td>
                                    <td class="spaced">0,82,40</td>
                                    <td style="background:rgb(0,82,40);width: 100px;">
                                    </td>
                                    <td class="center">1801</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">682</td>
                                    <td>Cobalt Turq.Green</td>
                                    <td class="spaced">35,125,86</td>
                                    <td style="background:rgb(35,125,86);width: 100px;">
                                    </td>
                                    <td class="center">2190</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">701</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">49,51,54</td>
                                    <td style="background:rgb(49,51,54);width: 100px;">
                                    </td>
                                    <td class="center">1731</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-15" data-toggle="collapse" data-target="#datapnl-15">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Sennelier</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-15" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">116</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">250,250,245</td>
                                    <td style="background:rgb(250,250,245);width: 100px;">
                                    </td>
                                    <td class="center">2347</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">136</td>
                                    <td>Titanium Buff</td>
                                    <td class="spaced">238,218,172</td>
                                    <td style="background:rgb(238,218,172);width: 100px;">
                                    </td>
                                    <td class="center">2205</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">202</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">68,47,38</td>
                                    <td style="background:rgb(68,47,38);width: 100px;">
                                    </td>
                                    <td class="center">2096</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">205</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">50,42,33</td>
                                    <td style="background:rgb(50,42,33);width: 100px;">
                                    </td>
                                    <td class="center">1883</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">208</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">125,80,35</td>
                                    <td style="background:rgb(125,80,35);width: 100px;">
                                    </td>
                                    <td class="center">1819</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">211</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">95,40,20</td>
                                    <td style="background:rgb(95,40,20);width: 100px;">
                                    </td>
                                    <td class="center">2070</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">252</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">168,110,40</td>
                                    <td style="background:rgb(168,110,40);width: 100px;">
                                    </td>
                                    <td class="center">2246</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">254</td>
                                    <td>Light Yellow Ochre</td>
                                    <td class="spaced">235,166,51</td>
                                    <td style="background:rgb(235,166,51);width: 100px;">
                                    </td>
                                    <td class="center">2377</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">305</td>
                                    <td>Cerulean Blue</td>
                                    <td class="spaced">0,90,136</td>
                                    <td style="background:rgb(0,90,136);width: 100px;">
                                    </td>
                                    <td class="center">3057</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">307</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">36,68,131</td>
                                    <td style="background:rgb(36,68,131);width: 100px;">
                                    </td>
                                    <td class="center">2285</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">312</td>
                                    <td>Ultramarine Light</td>
                                    <td class="spaced">15,12,79</td>
                                    <td style="background:rgb(15,12,79);width: 100px;">
                                    </td>
                                    <td class="center">2230</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">314</td>
                                    <td>French Ultramarine</td>
                                    <td class="spaced">22,17,54</td>
                                    <td style="background:rgb(22,17,54);width: 100px;">
                                    </td>
                                    <td class="center">2026</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">318</td>
                                    <td>Prussian Blue</td>
                                    <td class="spaced">35,41,42</td>
                                    <td style="background:rgb(35,41,42);width: 100px;">
                                    </td>
                                    <td class="center">2055</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">326</td>
                                    <td>Phthalo Blue</td>
                                    <td class="spaced">56,55,68</td>
                                    <td style="background:rgb(56,55,68);width: 100px;">
                                    </td>
                                    <td class="center">1821</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">339</td>
                                    <td>Turquoise Light</td>
                                    <td class="spaced">0,166,174</td>
                                    <td style="background:rgb(0,166,174);width: 100px;">
                                    </td>
                                    <td class="center">2605</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">471</td>
                                    <td>Madder Brown</td>
                                    <td class="spaced">66,35,26</td>
                                    <td style="background:rgb(66,35,26);width: 100px;">
                                    </td>
                                    <td class="center">1325</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">501</td>
                                    <td>Lemon Yellow</td>
                                    <td class="spaced">251,214,0</td>
                                    <td style="background:rgb(251,214,0);width: 100px;">
                                    </td>
                                    <td class="center">1618</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">529</td>
                                    <td>Cadmiium Yellow Light</td>
                                    <td class="spaced">255,210,0</td>
                                    <td style="background:rgb(255,210,0);width: 100px;">
                                    </td>
                                    <td class="center">2367</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">531</td>
                                    <td>Cadmium Yellow Medium</td>
                                    <td class="spaced"></td>
                                    <td style="background:rgb();width: 100px;">
                                    </td>
                                    <td class="center">2500</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">533</td>
                                    <td>Cadmium Yellow Deep</td>
                                    <td class="spaced">255,155,0</td>
                                    <td style="background:rgb(255,155,0);width: 100px;">
                                    </td>
                                    <td class="center">2407</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">535</td>
                                    <td>Cadmium Yellow Lemon</td>
                                    <td class="spaced">251,223,0</td>
                                    <td style="background:rgb(251,223,0);width: 100px;">
                                    </td>
                                    <td class="center">2318</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">537</td>
                                    <td>Cadmium Yellow Orange</td>
                                    <td class="spaced">255,131,0</td>
                                    <td style="background:rgb(255,131,0);width: 100px;">
                                    </td>
                                    <td class="center">2427</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">559</td>
                                    <td>Auroline</td>
                                    <td class="spaced">214,159,0</td>
                                    <td style="background:rgb(214,159,0);width: 100px;">
                                    </td>
                                    <td class="center">2075</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">590</td>
                                    <td>Indian Yellow Orange</td>
                                    <td class="spaced">230,124,0</td>
                                    <td style="background:rgb(230,124,0);width: 100px;">
                                    </td>
                                    <td class="center">1672</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">605</td>
                                    <td>Cadmium Red Light</td>
                                    <td class="spaced">202,20,19</td>
                                    <td style="background:rgb(202,20,19);width: 100px;">
                                    </td>
                                    <td class="center">2440</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">606</td>
                                    <td>Cadmium Red Deep</td>
                                    <td class="spaced">163,0,28</td>
                                    <td style="background:rgb(163,0,28);width: 100px;">
                                    </td>
                                    <td class="center">2582</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">607</td>
                                    <td>Cadmium Red Medium</td>
                                    <td class="spaced">178,0,18</td>
                                    <td style="background:rgb(178,0,18);width: 100px;">
                                    </td>
                                    <td class="center">2360</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">609</td>
                                    <td>Cadmium Red Orange</td>
                                    <td class="spaced">242,76,0</td>
                                    <td style="background:rgb(242,76,0);width: 100px;">
                                    </td>
                                    <td class="center">2415</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">636</td>
                                    <td>Sennelier Red</td>
                                    <td class="spaced">206,14,7</td>
                                    <td style="background:rgb(206,14,7);width: 100px;">
                                    </td>
                                    <td class="center">2257</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">639</td>
                                    <td>Carmine Deep</td>
                                    <td class="spaced">131,7,23</td>
                                    <td style="background:rgb(131,7,23);width: 100px;">
                                    </td>
                                    <td class="center">1920</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">688</td>
                                    <td>Crimson Lake</td>
                                    <td class="spaced">139,16,26</td>
                                    <td style="background:rgb(139,16,26);width: 100px;">
                                    </td>
                                    <td class="center">1286</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">695</td>
                                    <td>Alizarin Crimson</td>
                                    <td class="spaced">78,42,43</td>
                                    <td style="background:rgb(78,42,43);width: 100px;">
                                    </td>
                                    <td class="center">1281</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">699</td>
                                    <td>Perm.Alizarin Crimson Deep</td>
                                    <td class="spaced">59,29,27</td>
                                    <td style="background:rgb(59,29,27);width: 100px;">
                                    </td>
                                    <td class="center">1706</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">755</td>
                                    <td>Ivory Black</td>
                                    <td class="spaced">25,25,24</td>
                                    <td style="background:rgb(25,25,24);width: 100px;">
                                    </td>
                                    <td class="center">1567</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">759</td>
                                    <td>Mars Black</td>
                                    <td class="spaced">22,20,18</td>
                                    <td style="background:rgb(22,20,18);width: 100px;">
                                    </td>
                                    <td class="center">1844</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">815</td>
                                    <td>Chromium Oxide Green</td>
                                    <td class="spaced">74,112,66</td>
                                    <td style="background:rgb(74,112,66);width: 100px;">
                                    </td>
                                    <td class="center">2498</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">817</td>
                                    <td>Phthalo Green Warm</td>
                                    <td class="spaced">0,46,37</td>
                                    <td style="background:rgb(0,46,37);width: 100px;">
                                    </td>
                                    <td class="center">2270</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">818</td>
                                    <td>Phthalo Green Cool</td>
                                    <td class="spaced">34,45,48</td>
                                    <td style="background:rgb(34,45,48);width: 100px;">
                                    </td>
                                    <td class="center">1335</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">833</td>
                                    <td>Cobalt Green Light</td>
                                    <td class="spaced">17,119,106</td>
                                    <td style="background:rgb(17,119,106);width: 100px;">
                                    </td>
                                    <td class="center">2526</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">835</td>
                                    <td>Cobalt Green Deep</td>
                                    <td class="spaced">8,76,60</td>
                                    <td style="background:rgb(8,76,60);width: 100px;">
                                    </td>
                                    <td class="center">3090</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">837</td>
                                    <td>Viridian</td>
                                    <td class="spaced">0,68,59</td>
                                    <td style="background:rgb(0,68,59);width: 100px;">
                                    </td>
                                    <td class="center">1712</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">915</td>
                                    <td>Manganese Violet</td>
                                    <td class="spaced">57,20,65</td>
                                    <td style="background:rgb(57,20,65);width: 100px;">
                                    </td>
                                    <td class="center">1945</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">916</td>
                                    <td>Ultramarine Violet</td>
                                    <td class="spaced">28,25,41</td>
                                    <td style="background:rgb(28,25,41);width: 100px;">
                                    </td>
                                    <td class="center">1955</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">917</td>
                                    <td>Dioxazine Violet</td>
                                    <td class="spaced">57,57,55</td>
                                    <td style="background:rgb(57,57,55);width: 100px;">
                                    </td>
                                    <td class="center">1989</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">941</td>
                                    <td>Magenta</td>
                                    <td class="spaced">73,28,39</td>
                                    <td style="background:rgb(73,28,39);width: 100px;">
                                    </td>
                                    <td class="center">2253</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">953</td>
                                    <td>Ultramarine Rose</td>
                                    <td class="spaced">65,30,69</td>
                                    <td style="background:rgb(65,30,69);width: 100px;">
                                    </td>
                                    <td class="center">2314</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-16" data-toggle="collapse" data-target="#datapnl-16">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>System 3 Original Acrylic - Daler Rowney</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-16" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">6</td>
                                    <td>Zinc Mixing White</td>
                                    <td class="spaced">247,250,245</td>
                                    <td style="background:rgb(247,250,245);width: 100px;">
                                    </td>
                                    <td class="center">1587</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">9</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">251,251,246</td>
                                    <td style="background:rgb(251,251,246);width: 100px;">
                                    </td>
                                    <td class="center">1615</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">24</td>
                                    <td>Buff Titanium</td>
                                    <td class="spaced">213,195,161</td>
                                    <td style="background:rgb(213,195,161);width: 100px;">
                                    </td>
                                    <td class="center">1451</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">36</td>
                                    <td>Mars Black</td>
                                    <td class="spaced">51,49,50</td>
                                    <td style="background:rgb(51,49,50);width: 100px;">
                                    </td>
                                    <td class="center">1618</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">40</td>
                                    <td>Process Black</td>
                                    <td class="spaced">49,49,49</td>
                                    <td style="background:rgb(49,49,49);width: 100px;">
                                    </td>
                                    <td class="center">1489</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">110</td>
                                    <td>Cobalt Blue (hue)</td>
                                    <td class="spaced">43,91,192</td>
                                    <td style="background:rgb(43,91,192);width: 100px;">
                                    </td>
                                    <td class="center">1389</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">112</td>
                                    <td>Coeruleum Blue (hue)</td>
                                    <td class="spaced">0,109,161</td>
                                    <td style="background:rgb(0,109,161);width: 100px;">
                                    </td>
                                    <td class="center">1602</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">120</td>
                                    <td>Process Cyan</td>
                                    <td class="spaced">44 51 85</td>
                                    <td style="background:rgb(44 51 85);width: 100px;">
                                    </td>
                                    <td class="center">1526</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">123</td>
                                    <td>Ultramarine</td>
                                    <td class="spaced">51,48,80</td>
                                    <td style="background:rgb(51,48,80);width: 100px;">
                                    </td>
                                    <td class="center">1600</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">134</td>
                                    <td>Prussian Blue (hue)</td>
                                    <td class="spaced">46,46,60</td>
                                    <td style="background:rgb(46,46,60);width: 100px;">
                                    </td>
                                    <td class="center">1516</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">142</td>
                                    <td>Phthalo Blue</td>
                                    <td class="spaced">49,45,81</td>
                                    <td style="background:rgb(49,45,81);width: 100px;">
                                    </td>
                                    <td class="center">1501</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">221</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">123,62,51</td>
                                    <td style="background:rgb(123,62,51);width: 100px;">
                                    </td>
                                    <td class="center">1360</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">223</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">75,60,55</td>
                                    <td style="background:rgb(75,60,55);width: 100px;">
                                    </td>
                                    <td class="center">1535</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">247</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">67,60,55</td>
                                    <td style="background:rgb(67,60,55);width: 100px;">
                                    </td>
                                    <td class="center">1549</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">352</td>
                                    <td>Hooker&#x2019;s Green</td>
                                    <td class="spaced">46,62,52</td>
                                    <td style="background:rgb(46,62,52);width: 100px;">
                                    </td>
                                    <td class="center">1486</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">361</td>
                                    <td>Phthalo Green</td>
                                    <td class="spaced">38,58,58</td>
                                    <td style="background:rgb(38,58,58);width: 100px;">
                                    </td>
                                    <td class="center">1573</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">367</td>
                                    <td>Oxide of Chromium Green</td>
                                    <td class="spaced">81,117,76</td>
                                    <td style="background:rgb(81,117,76);width: 100px;">
                                    </td>
                                    <td class="center">1614</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">375</td>
                                    <td>Sap Green</td>
                                    <td class="spaced">42,75,49</td>
                                    <td style="background:rgb(42,75,49);width: 100px;">
                                    </td>
                                    <td class="center">1377</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">408</td>
                                    <td>Deep Violet</td>
                                    <td class="spaced">57,51,53</td>
                                    <td style="background:rgb(57,51,53);width: 100px;">
                                    </td>
                                    <td class="center">1507</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">412</td>
                                    <td>Process Magenta</td>
                                    <td class="spaced">138,47,68</td>
                                    <td style="background:rgb(138,47,68);width: 100px;">
                                    </td>
                                    <td class="center">1516</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">503</td>
                                    <td>Cadmium Red (hue)</td>
                                    <td class="spaced">189,45,44</td>
                                    <td style="background:rgb(189,45,44);width: 100px;">
                                    </td>
                                    <td class="center">1511</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">504</td>
                                    <td>CadmiumRedDeep</td>
                                    <td class="spaced">159,43,44</td>
                                    <td style="background:rgb(159,43,44);width: 100px;">
                                    </td>
                                    <td class="center">1494</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">588</td>
                                    <td>Vermilion (hue)</td>
                                    <td class="spaced">210,45,37</td>
                                    <td style="background:rgb(210,45,37);width: 100px;">
                                    </td>
                                    <td class="center">1387</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">618</td>
                                    <td>Cadmium Yellow D Hue</td>
                                    <td class="spaced">238,139,0</td>
                                    <td style="background:rgb(238,139,0);width: 100px;">
                                    </td>
                                    <td class="center">1494</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">619</td>
                                    <td>Cadmium Orange (hue)</td>
                                    <td class="spaced">227,71,37</td>
                                    <td style="background:rgb(227,71,37);width: 100px;">
                                    </td>
                                    <td class="center">1270</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">651</td>
                                    <td>Lemon Yellow</td>
                                    <td class="spaced">241,222,0</td>
                                    <td style="background:rgb(241,222,0);width: 100px;">
                                    </td>
                                    <td class="center">1461</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">663</td>
                                    <td>Yellow Ochre</td>
                                    <td class="spaced">189,137,62</td>
                                    <td style="background:rgb(189,137,62);width: 100px;">
                                    </td>
                                    <td class="center">1285</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">667</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">163,105,59</td>
                                    <td style="background:rgb(163,105,59);width: 100px;">
                                    </td>
                                    <td class="center">1441</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">675</td>
                                    <td>Process Yellow</td>
                                    <td class="spaced">254,208,0</td>
                                    <td style="background:rgb(254,208,0);width: 100px;">
                                    </td>
                                    <td class="center">1443</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="panel-group">
            <div class="panel panel-default">
                <div class="panel-heading" id="ph-17" data-toggle="collapse" data-target="#datapnl-17">
                    <h2 class="panel-title">
                        <i class="fa fa-tint"></i>
                        <span>Vallejo Acrylic Studio</span>
                    </h2>
                    <i class="panel-arrow fa fa-angle-down"></i>
                </div>
                <div id="datapnl-17" class="panel-collapse collapse">
                    <table>
                        <tbody>
                            <tr>
                                <th style="min-width:60px;">ID</th>
                                <th style="width:360px; min-width: 200px;">Name</th>
                                <th style="width:150px; min-width: 100px;">RGB</th>
                                <th style="min-width: 100px;"></th>
                                <th style="min-width: 60px;">Density</th>
                                <th style="min-width: 60px;">Opacity</th>
                                <th style="min-width: 100px;">Permanence</th>
                                <th style="min-width: 200px;">IndexName</th>
                            </tr>
                                <tr>
                                    <td class="center">1</td>
                                    <td>Cadmium Lemon Yellow</td>
                                    <td class="spaced">246,226,0</td>
                                    <td style="background:rgb(246,226,0);width: 100px;">
                                    </td>
                                    <td class="center">1219</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">2</td>
                                    <td>Cadmium Red</td>
                                    <td class="spaced">172,23,28</td>
                                    <td style="background:rgb(172,23,28);width: 100px;">
                                    </td>
                                    <td class="center">1251</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">3</td>
                                    <td>Naphtol Crimson</td>
                                    <td class="spaced">143,27,37</td>
                                    <td style="background:rgb(143,27,37);width: 100px;">
                                    </td>
                                    <td class="center">1254</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">4</td>
                                    <td>Ultramarine Blue</td>
                                    <td class="spaced">42,41,77</td>
                                    <td style="background:rgb(42,41,77);width: 100px;">
                                    </td>
                                    <td class="center">1401</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">5</td>
                                    <td>Phthalo Blue</td>
                                    <td class="spaced">39,33,78</td>
                                    <td style="background:rgb(39,33,78);width: 100px;">
                                    </td>
                                    <td class="center">1229</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">6</td>
                                    <td>Phthalo Green</td>
                                    <td class="spaced">22,47,53</td>
                                    <td style="background:rgb(22,47,53);width: 100px;">
                                    </td>
                                    <td class="center">1253</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">8</td>
                                    <td>Mars Yellow</td>
                                    <td class="spaced">194,134,33</td>
                                    <td style="background:rgb(194,134,33);width: 100px;">
                                    </td>
                                    <td class="center">1323</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">10</td>
                                    <td>Mars Red</td>
                                    <td class="spaced">134,55,45</td>
                                    <td style="background:rgb(134,55,45);width: 100px;">
                                    </td>
                                    <td class="center">1432</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">12</td>
                                    <td>Mars Black</td>
                                    <td class="spaced">48,47,47</td>
                                    <td style="background:rgb(48,47,47);width: 100px;">
                                    </td>
                                    <td class="center">1387</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">13</td>
                                    <td>Azo Yellow Orange</td>
                                    <td class="spaced">223,132,0</td>
                                    <td style="background:rgb(223,132,0);width: 100px;">
                                    </td>
                                    <td class="center">1212</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">14</td>
                                    <td>Permanent Violet</td>
                                    <td class="spaced">43,38,39</td>
                                    <td style="background:rgb(43,38,39);width: 100px;">
                                    </td>
                                    <td class="center">1249</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">15</td>
                                    <td>Orange</td>
                                    <td class="spaced">220,58,34</td>
                                    <td style="background:rgb(220,58,34);width: 100px;">
                                    </td>
                                    <td class="center">1245</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">16</td>
                                    <td>Sap Green</td>
                                    <td class="spaced">37,52,40</td>
                                    <td style="background:rgb(37,52,40);width: 100px;">
                                    </td>
                                    <td class="center">1245</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">17</td>
                                    <td>Raw Umber</td>
                                    <td class="spaced">96,81,62</td>
                                    <td style="background:rgb(96,81,62);width: 100px;">
                                    </td>
                                    <td class="center">1363</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">18</td>
                                    <td>Burnt Umber</td>
                                    <td class="spaced">82,59,51</td>
                                    <td style="background:rgb(82,59,51);width: 100px;">
                                    </td>
                                    <td class="center">1386</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">19</td>
                                    <td>Raw Sienna</td>
                                    <td class="spaced">163,109,40</td>
                                    <td style="background:rgb(163,109,40);width: 100px;">
                                    </td>
                                    <td class="center">1325</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">20</td>
                                    <td>Burnt Sienna</td>
                                    <td class="spaced">131,63,45</td>
                                    <td style="background:rgb(131,63,45);width: 100px;">
                                    </td>
                                    <td class="center">1379</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">21</td>
                                    <td>Naples Yellow</td>
                                    <td class="spaced">238,189,104</td>
                                    <td style="background:rgb(238,189,104);width: 100px;">
                                    </td>
                                    <td class="center">1413</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">22</td>
                                    <td>Cadmium Yellow Deep</td>
                                    <td class="spaced">255,187,0</td>
                                    <td style="background:rgb(255,187,0);width: 100px;">
                                    </td>
                                    <td class="center">1249</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">23</td>
                                    <td>Magenta</td>
                                    <td class="spaced">125,16,61</td>
                                    <td style="background:rgb(125,16,61);width: 100px;">
                                    </td>
                                    <td class="center">1244</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">24</td>
                                    <td>Primary Blue</td>
                                    <td class="spaced">0,141,206</td>
                                    <td style="background:rgb(0,141,206);width: 100px;">
                                    </td>
                                    <td class="center">1390</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">25</td>
                                    <td>Cobalt Blue</td>
                                    <td class="spaced">50,97,192</td>
                                    <td style="background:rgb(50,97,192);width: 100px;">
                                    </td>
                                    <td class="center">1424</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">26</td>
                                    <td>Rose Madder</td>
                                    <td class="spaced">114,29,30</td>
                                    <td style="background:rgb(114,29,30);width: 100px;">
                                    </td>
                                    <td class="center">1252</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">41</td>
                                    <td>Titanium White</td>
                                    <td class="spaced">243,243,246</td>
                                    <td style="background:rgb(243,243,246);width: 100px;">
                                    </td>
                                    <td class="center">1409</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">43</td>
                                    <td>Cadmium Yellow Pale</td>
                                    <td class="spaced">251,205,0</td>
                                    <td style="background:rgb(251,205,0);width: 100px;">
                                    </td>
                                    <td class="center">1193</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">45</td>
                                    <td>Dark Cad Red</td>
                                    <td class="spaced">148,43,32</td>
                                    <td style="background:rgb(148,43,32);width: 100px;">
                                    </td>
                                    <td class="center">1268</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                                <tr>
                                    <td class="center">46</td>
                                    <td>Prussian Blue Phtalo</td>
                                    <td class="spaced">40,39,51</td>
                                    <td style="background:rgb(40,39,51);width: 100px;">
                                    </td>
                                    <td class="center">1382</td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                    <td class="center"></td>
                                </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    <h3>Historical and Common Color Names</h3>
    <div class="info-box">
        <p>
            The colors below was measured digitally, so they should be adjusted to a smaller color space before being converted into artists' paints with PaintMaker.
            <br/>
            We have done that in the columns on the right.
        </p>
    </div>
    <div class="panel-group">
        <div class="panel panel-default">
            <div class="panel-heading" id="ph-18" data-toggle="collapse" data-target="#datapnl-18">
                <h2 class="panel-title">
                    <i class="fa fa-tint"></i>
                    Common Color Names & Values
                </h2>
                <i class="panel-arrow fa fa-angle-down"></i>
            </div>
            <div id="datapnl-18" class="panel-collapse collapse in">
                <table>
                    <tbody>
                        <tr>
                            <th style="width:30px;"></th>
                            <th style="width:160px;">Name</th>
                            <th style="width:150px;">HEX</th>
                            <th style="width:150px;text-align:left;">RGB</th>
                            <th></th>
                            <th style="width:30px;"></th>
                            <th style="width:150px;text-align:left;">Adjusted HEX</th>
                            <th style="width:150px;text-align:left;">Adjusted RGB</th>
                            <th></th>
                            <th style="width:10px;"></th>
                        </tr>
                            <tr>
                                <td></td>
                                <td>Aquamarine</td>
                                <td class="spaced">#7fffd4</td>
                                <td class="spaced">127,255,212</td>
                                <td style="background:rgb(127,255,212);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#92ffda</td>
                                <td class="spaced">146,255,218</td>
                                <td style="background:rgb(146,255,218);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Antiquewhite</td>
                                <td class="spaced">#faebd7</td>
                                <td class="spaced">250,235,215</td>
                                <td style="background:rgb(250,235,215);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#fbeedd</td>
                                <td class="spaced">251,238,221</td>
                                <td style="background:rgb(251,238,221);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Beige</td>
                                <td class="spaced">#f5f5dc</td>
                                <td class="spaced">245,245,220</td>
                                <td style="background:rgb(245,245,220);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#f6f6e1</td>
                                <td class="spaced">246,246,225</td>
                                <td style="background:rgb(246,246,225);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Cadetblue</td>
                                <td class="spaced">#5f9ea0</td>
                                <td class="spaced">95,158,160</td>
                                <td style="background:rgb(95,158,160);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#77acae</td>
                                <td class="spaced">119,172,174</td>
                                <td style="background:rgb(119,172,174);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Coral</td>
                                <td class="spaced">#ff7f50</td>
                                <td class="spaced">255,127,80</td>
                                <td style="background:rgb(255,127,80);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#ff926a</td>
                                <td class="spaced">255,146,106</td>
                                <td style="background:rgb(255,146,106);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Cornflowerblue</td>
                                <td class="spaced">#6495ed</td>
                                <td class="spaced">100,149,237</td>
                                <td style="background:rgb(100,149,237);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#7ba5f0</td>
                                <td class="spaced">123,165,240</td>
                                <td style="background:rgb(123,165,240);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Cornsilk</td>
                                <td class="spaced">#fff8dc</td>
                                <td class="spaced">255,248,220</td>
                                <td style="background:rgb(255,248,220);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#fff9e1</td>
                                <td class="spaced">255,249,225</td>
                                <td style="background:rgb(255,249,225);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Firebrick</td>
                                <td class="spaced">#b22222</td>
                                <td class="spaced">178,34,34</td>
                                <td style="background:rgb(178,34,34);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#bd4343</td>
                                <td class="spaced">189,67,67</td>
                                <td style="background:rgb(189,67,67);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Forestgreen</td>
                                <td class="spaced">#228b22</td>
                                <td class="spaced">34,139,34</td>
                                <td style="background:rgb(34,139,34);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#439c43</td>
                                <td class="spaced">67,156,67</td>
                                <td style="background:rgb(67,156,67);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Gainsboro</td>
                                <td class="spaced">#dcdcdc</td>
                                <td class="spaced">220,220,220</td>
                                <td style="background:rgb(220,220,220);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#e1e1e1</td>
                                <td class="spaced">225,225,225</td>
                                <td style="background:rgb(225,225,225);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Gold</td>
                                <td class="spaced">#ffd700</td>
                                <td class="spaced">255,215,0</td>
                                <td style="background:rgb(255,215,0);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#ffdd26</td>
                                <td class="spaced">255,221,38</td>
                                <td style="background:rgb(255,221,38);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Honeydew</td>
                                <td class="spaced">#f0fff0</td>
                                <td class="spaced">240,255,240</td>
                                <td style="background:rgb(240,255,240);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#f2fff2</td>
                                <td class="spaced">242,255,242</td>
                                <td style="background:rgb(242,255,242);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Khaki</td>
                                <td class="spaced">#f0e68c</td>
                                <td class="spaced">240,230,140</td>
                                <td style="background:rgb(240,230,140);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#f2ea9d</td>
                                <td class="spaced">242,234,157</td>
                                <td style="background:rgb(242,234,157);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Lavender</td>
                                <td class="spaced">#e6e6fa</td>
                                <td class="spaced">230,230,250</td>
                                <td style="background:rgb(230,230,250);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#eaeafb</td>
                                <td class="spaced">234,234,251</td>
                                <td style="background:rgb(234,234,251);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Lavenderblush</td>
                                <td class="spaced">#fff0f5</td>
                                <td class="spaced">255,240,245</td>
                                <td style="background:rgb(255,240,245);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#fff2f6</td>
                                <td class="spaced">255,242,246</td>
                                <td style="background:rgb(255,242,246);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Lawngreen</td>
                                <td class="spaced">#7cfc00</td>
                                <td class="spaced">124,252,0</td>
                                <td style="background:rgb(124,252,0);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#90fc26</td>
                                <td class="spaced">144,252,38</td>
                                <td style="background:rgb(144,252,38);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Lemonchiffon</td>
                                <td class="spaced">#fffacd</td>
                                <td class="spaced">255,250,205</td>
                                <td style="background:rgb(255,250,205);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#fffbd4</td>
                                <td class="spaced">255,251,212</td>
                                <td style="background:rgb(255,251,212);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Lightsalmon</td>
                                <td class="spaced">#ffa07a</td>
                                <td class="spaced">255,160,122</td>
                                <td style="background:rgb(255,160,122);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#ffae8e</td>
                                <td class="spaced">255,174,142</td>
                                <td style="background:rgb(255,174,142);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Linen</td>
                                <td class="spaced">#faf0e6</td>
                                <td class="spaced">250,240,230</td>
                                <td style="background:rgb(250,240,230);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#fbf2ea</td>
                                <td class="spaced">251,242,234,</td>
                                <td style="background:rgb(251,242,234,);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Maroon</td>
                                <td class="spaced">#800000</td>
                                <td class="spaced">128,0,0</td>
                                <td style="background:rgb(128,0,0);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#932626</td>
                                <td class="spaced">147,38,38</td>
                                <td style="background:rgb(147,38,38);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Midnightblue</td>
                                <td class="spaced">#191970</td>
                                <td class="spaced">25,25,112</td>
                                <td style="background:rgb(25,25,112);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#3b3b85</td>
                                <td class="spaced">59,59,133</td>
                                <td style="background:rgb(59,59,133);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Mintcream</td>
                                <td class="spaced">#f5fffa</td>
                                <td class="spaced">240,255,250</td>
                                <td style="background:rgb(240,255,250);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#f5fffa</td>
                                <td class="spaced">246,255,251</td>
                                <td style="background:rgb(246,255,251);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Mistyrose</td>
                                <td class="spaced">#ffe4e1</td>
                                <td class="spaced">255,228,225</td>
                                <td style="background:rgb(255,228,225);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#ffe8e5</td>
                                <td class="spaced">255,232,229</td>
                                <td style="background:rgb(255,232,229);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Moccasin</td>
                                <td class="spaced">#ffe4b5</td>
                                <td class="spaced">255,228,181</td>
                                <td style="background:rgb(255,228,181);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#ffe8c0</td>
                                <td class="spaced">255,232,192</td>
                                <td style="background:rgb(255,232,192);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Navy</td>
                                <td class="spaced">#000080</td>
                                <td class="spaced">0,0,128</td>
                                <td style="background:rgb(0,0,128);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#262693</td>
                                <td class="spaced">38,38,147</td>
                                <td style="background:rgb(38,38,147);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Oldlace</td>
                                <td class="spaced">#fdf5e6</td>
                                <td class="spaced">253,245,230</td>
                                <td style="background:rgb(253,245,230);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#fdf6ea</td>
                                <td class="spaced">253,246,234</td>
                                <td style="background:rgb(253,246,234);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Olive</td>
                                <td class="spaced">#808000</td>
                                <td class="spaced">128,128,0</td>
                                <td style="background:rgb(128,128,0);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#939326</td>
                                <td class="spaced">147,147,38</td>
                                <td style="background:rgb(147,147,38);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Olivedrab</td>
                                <td class="spaced">#6b8e23</td>
                                <td class="spaced">107,142,35</td>
                                <td style="background:rgb(107,142,35);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#819f44</td>
                                <td class="spaced">129,159,68</td>
                                <td style="background:rgb(129,159,68);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Orchid</td>
                                <td class="spaced">#da70d6</td>
                                <td class="spaced">218,112,214</td>
                                <td style="background:rgb(218,112,214);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#e085dc</td>
                                <td class="spaced">224,133,220</td>
                                <td style="background:rgb(224,133,220);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Palegoldenrod</td>
                                <td class="spaced">#eee8aa</td>
                                <td class="spaced">238,232,170</td>
                                <td style="background:rgb(238,232,170);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#f1ebb7</td>
                                <td class="spaced">241,235,183</td>
                                <td style="background:rgb(241,235,183);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Palegreen</td>
                                <td class="spaced">#98fb98</td>
                                <td class="spaced">152,251,152</td>
                                <td style="background:rgb(152,251,152);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#a7fca7</td>
                                <td class="spaced">167,252,167</td>
                                <td style="background:rgb(167,252,167);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Peachpuff</td>
                                <td class="spaced">#ffdab9</td>
                                <td class="spaced">255,218,185</td>
                                <td style="background:rgb(255,218,185);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#ffe0c3</td>
                                <td class="spaced">255,224,195</td>
                                <td style="background:rgb(255,224,195);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Peru</td>
                                <td class="spaced">#cd853f</td>
                                <td class="spaced">205,133,63</td>
                                <td style="background:rgb(205,133,63);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#d4975c</td>
                                <td class="spaced">212,151,92</td>
                                <td style="background:rgb(212,151,92);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Pink</td>
                                <td class="spaced">#ffc0cb</td>
                                <td class="spaced">255,192,203</td>
                                <td style="background:rgb(255,192,203);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#ffc9d3</td>
                                <td class="spaced">255,201,211,</td>
                                <td style="background:rgb(255,201,211,);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Plum</td>
                                <td class="spaced">#dda0dd</td>
                                <td class="spaced">221,160,221</td>
                                <td style="background:rgb(221,160,221);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#e2aee2</td>
                                <td class="spaced">226,174,226</td>
                                <td style="background:rgb(226,174,226);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Royalblue</td>
                                <td class="spaced">#4169e1</td>
                                <td class="spaced">65,105,225</td>
                                <td style="background:rgb(65,105,225);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#5d7fe5</td>
                                <td class="spaced">93,127,229</td>
                                <td style="background:rgb(93,127,229);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Saddlebrown</td>
                                <td class="spaced">#8b4513</td>
                                <td class="spaced">139,69,19</td>
                                <td style="background:rgb(139,69,19);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#9c6136</td>
                                <td class="spaced">156,97,54</td>
                                <td style="background:rgb(156,97,54);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Salmon</td>
                                <td class="spaced">#fa8072</td>
                                <td class="spaced">250,128,114</td>
                                <td style="background:rgb(250,128,114);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#fb9387</td>
                                <td class="spaced">251,147,135</td>
                                <td style="background:rgb(251,147,135);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Seagreen</td>
                                <td class="spaced">#2e8b57</td>
                                <td class="spaced">46,139,87</td>
                                <td style="background:rgb(46,139,87);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#4d9c70</td>
                                <td class="spaced">77,156,112</td>
                                <td style="background:rgb(77,156,112);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Seashell</td>
                                <td class="spaced">#fff5ee</td>
                                <td class="spaced">255,245,238</td>
                                <td style="background:rgb(255,245,238);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#fff6f1</td>
                                <td class="spaced">255,246,241</td>
                                <td style="background:rgb(255,246,241);width: 100px;"></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>Slategray</td>
                                <td class="spaced">#708090</td>
                                <td class="spaced">112,128,144</td>
                                <td style="background:rgb(112,128,144);width: 100px;"></td>
                                <td></td>
                                <td class="spaced">#8593a1</td>
                                <td class="spaced">133,147,161</td>
                                <td style="background:rgb(133,147,161);width: 100px;"></td>
                                <td></td>
                            </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

        </article>

        <!-- Footer -->
        <footer>
            <div class="footer-divider">
                
                    <h6 id="newsletter-label">FIND OUT WHEN WE RELEASE NEW PAINT SETS AND NEW FEATURES!</h6>
                    <form id="newsletter-form" method="post" role="form" action="/account/subtonewsletter">
                        <div class="input-group">
                            <span class="input-group-addon"><i class="fa fa-envelope"></i></span>
                            <input id="newsletter-input" name="Email" type="email" class="form-control" placeholder="E-mail to receive newsletter" required>
                            <span class="input-group-btn">
                                <button id="newsletter-button" type="submit" class="btn" required>Subscribe</button>
                            </span>
                            <span class="welcome-sign">Thank you! You are now subscribed to our newsletter.</span>
                        </div>
                    <input name="__RequestVerificationToken" type="hidden" value="CfDJ8LuMd1jhCNJKrYU1KYetoP4TrmilycGwbJQ6ARQdNbe17AMKpr8fmK5IkjdyON-bTAhhH2OgYqDHU7x8POdwLV_T6rC-l6Y1cp7Cs0mFNZuGGx66TtWYXEfCcJvEJMkmGSRFnanxUVK96x8KU7w-VXg" /></form>
                    <h6 id="social-label">SHARE PAINTMAKER WITH THE WORLD</h6>


<ul class="social-links hidden-print" url="https://sensuallogic.com/artistcolordata">
    <li>
        <a target="_blank" href="https://facebook.com/sharer.php?u=https://sensuallogic.com/artistcolordata" class="social facebook">
            <div>
                <span>LIKE</span>
            </div>
        </a>
    </li>
    <li>
        <a target="_blank" href="https://twitter.com/intent/tweet?url=https://sensuallogic.com/artistcolordata&amp;amp;text=Mix Fine Artist Colors In Your Browser&amp;amp;via=sensuallogic" class="social twitter">
            <div>
                <span>TWEET</span>
            </div>
        </a>
    </li>
    <li>
        <a target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;amp;url=https://sensuallogic.com/artistcolordata&amp;amp;title=Mix Fine Artist Colors In Your Browser" class="social linkedin">
            <div>
                <span>SHARE</span>
            </div>
        </a>
    </li>
</ul>

            </div>
            <div class="footer-content">
                <a class="follow-icon" href="mailto:sensualogic@gmail.com" title="Send us a mail"><i class="fa fa-envelope" style="font-size:24px"></i></a>
                <img src="/images/svg/graffiti.svg" title="Find us via these links <3" width="54" height="54" />
                <a class="follow-icon" href="https://twitter.com/SensualLogic" title="Visit our twitter" target="_blank"><i class="fa fa-twitter" style="font-size:28px"></i></a>
            </div>
            <div id="site-info">
                <p><span class="cpy">&copy;</span> <span class="nbr">2016-24</span> - Sensual Logic // Web design by T. Scheel</p>
            </div>
        </footer>
    </div>

        <!-- Social Links -->
        <div class="social-links-container">
            

<ul class="social-links hidden-print" url="https://sensuallogic.com/artistcolordata">
    <li>
        <a target="_blank" href="https://facebook.com/sharer.php?u=https://sensuallogic.com/artistcolordata" class="social facebook">
            <div>
                <span>LIKE</span>
            </div>
        </a>
    </li>
    <li>
        <a target="_blank" href="https://twitter.com/intent/tweet?url=https://sensuallogic.com/artistcolordata&amp;amp;text=Mix Fine Artist Colors In Your Browser&amp;amp;via=sensuallogic" class="social twitter">
            <div>
                <span>TWEET</span>
            </div>
        </a>
    </li>
    <li>
        <a target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;amp;url=https://sensuallogic.com/artistcolordata&amp;amp;title=Mix Fine Artist Colors In Your Browser" class="social linkedin">
            <div>
                <span>SHARE</span>
            </div>
        </a>
    </li>
</ul>


        </div>

    <!-- Modal Placeholder-->
    <div id='sl-modal' class='modal bounce-in'>
        <div class="modal-dialog">
            <div id='sl-modal-content' class="modal-content">
            </div>
        </div>
    </div>

    <!-- Used for Ajax CSRF Post calls -->
    <input name="__RequestVerificationToken" type="hidden" value="CfDJ8LuMd1jhCNJKrYU1KYetoP4TrmilycGwbJQ6ARQdNbe17AMKpr8fmK5IkjdyON-bTAhhH2OgYqDHU7x8POdwLV_T6rC-l6Y1cp7Cs0mFNZuGGx66TtWYXEfCcJvEJMkmGSRFnanxUVK96x8KU7w-VXg" />

    <!-- Scripts -->
    <script type="text/javascript" src="https://js.stripe.com/v3/"></script>
    <script src="https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit" defer></script>

    
    
        <script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-2.1.4.min.js" integrity="sha384-8gBf6Y4YYq7Jx97PIqmTwLPin4hxIzQw5aDmUg/DDhul9fFpbbLcLh3nTIIDJKhx" crossorigin="anonymous">
        </script>
<script>(window.jQuery||document.write("\u003Cscript src=\u0022/lib/jquery/dist/jquery.min.js\u0022 integrity=\u0022sha384-8gBf6Y4YYq7Jx97PIqmTwLPin4hxIzQw5aDmUg/DDhul9fFpbbLcLh3nTIIDJKhx\u0022 crossorigin=\u0022anonymous\u0022\u003E\u003C/script\u003E"));</script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous">
        </script>
<script>(window.jQuery && window.jQuery.fn && window.jQuery.fn.modal||document.write("\u003Cscript src=\u0022/lib/bootstrap/dist/js/bootstrap.min.js\u0022 integrity=\u0022sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS\u0022 crossorigin=\u0022anonymous\u0022\u003E\u003C/script\u003E"));</script>        
        <script src="//www.googleadservices.com/pagead/conversion_async.js"></script>
        <script src="/js/site.min.js?v=6iybfGy1mGaTvXGM7PAKY0SIGuvYvPieU1EmvMgBGOQ"></script>
    

    

    <script>window.SenLogBaseUrl='';</script>
</body>
</html>

'''

# Step 2: Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find all the rows with color data (based on your provided HTML structure)
color_data = []

# Loop through all the color rows (assumed to be inside <tr> tags)

panels = soup.find("div", class_="panel-group")

for panel in panels:
    brand_category_title = soup.find("h2", class_="panel-title").find('span').text.strip()
    rows = soup.find_all('tr')

    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 0:  # Make sure it's a valid row
            # Extract the RGB values and color name
            color_name = columns[1].text.strip()  # Name is in the second column (index 1)
            rgb_values = columns[2].text.strip()  # RGB is in the third column (index 2)

            # Parse the RGB values
            try:
                rgb_values = tuple(map(int, rgb_values.split(',')))
                r = 255 if rgb_values[0] > 255 else rgb_values[0]
                g = 255 if rgb_values[1] > 255 else rgb_values[1]
                b = 255 if rgb_values[2] > 255 else rgb_values[2]
                rgb_values = (r, g, b)
            except ValueError:
                continue  # Skip invalid rows

            # Add the color data to the list
            color_data.append({
                'brand': brand_category_title,
                'name': color_name,
                'rgb': rgb_values
            })

# Step 4: Save the scraped data into a JSON file
with open('colors.json', 'w') as json_file:
    json.dump(color_data, json_file, indent=4)

print("Data scraped and saved to 'colors.json'")