from lxml import etree


def exportar_xml(xml, pretty_print=False):
    return etree.tostring(xml, encoding="unicode", pretty_print=pretty_print).replace("&lt;", "<").replace("&gt;", ">")
