import os
import zipfile
import xml.etree.ElementTree as ET

def parse_docx_structure(docx_path, out_txt_path):
    if not os.path.exists(docx_path):
        print(f"Error: {docx_path} does not exist.")
        return
        
    print(f"Parsing structure of {docx_path}...")
    
    # Namespaces
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }
    
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        # Read relationships
        rels_xml = zip_ref.read('word/_rels/document.xml.rels')
        rels_root = ET.fromstring(rels_xml)
        
        # Map rId -> image path
        rel_map = {}
        for rel in rels_root.iter('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
            rId = rel.attrib.get('Id')
            target = rel.attrib.get('Target')
            if 'media' in target:
                rel_map[rId] = os.path.basename(target)
                
        # Read main document
        doc_xml = zip_ref.read('word/document.xml')
        doc_root = ET.fromstring(doc_xml)
        
        body = doc_root.find('w:body', ns)
        if body is None:
            print("No w:body found in document.xml")
            return
            
        elements = []
        
        # We walk through body children
        for child in body:
            tag = child.tag.split('}')[-1]
            
            if tag == 'p': # Paragraph
                # Extract text
                texts = []
                for t in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                    if t.text:
                        texts.append(t.text)
                p_text = "".join(texts).strip()
                
                # Check for inline or anchored images in the paragraph
                p_images = []
                for drawing in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}drawing'):
                    for blip in drawing.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip'):
                        embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                        if embed_id in rel_map:
                            p_images.append(rel_map[embed_id])
                            
                # Also check w:drawing for other elements
                for ole in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}object'):
                    for im in ole.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}imagedata'):
                        rel_id = im.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                        if rel_id in rel_map:
                            p_images.append(rel_map[rel_id])
                
                elements.append({
                    'type': 'p',
                    'text': p_text,
                    'images': p_images
                })
                
            elif tag == 'tbl': # Table
                table_cells = []
                for row in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'):
                    row_data = []
                    for cell in row.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'):
                        cell_texts = []
                        for t in cell.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                            if t.text:
                                cell_texts.append(t.text)
                        row_data.append("".join(cell_texts).strip())
                    table_cells.append(row_data)
                
                elements.append({
                    'type': 'table',
                    'data': table_cells
                })
                
        print(f"Processed {len(elements)} block elements.")
        
        with open(out_txt_path, 'w', encoding='utf-8') as f:
            for idx, el in enumerate(elements):
                if el['type'] == 'p':
                    # Only write paragraphs with text or with images
                    if el['text'] or el['images']:
                        f.write(f"[{idx}] P: {el['text']}\n")
                        if el['images']:
                            f.write(f"      IMAGES: {', '.join(el['images'])}\n")
                elif el['type'] == 'table':
                    f.write(f"[{idx}] TABLE:\n")
                    for row in el['data']:
                        f.write(f"      ROW: {row}\n")
                # write a clean separator if anything was written
                if el['type'] == 'table' or el['text'] or el['images']:
                    f.write("\n")
                
        print(f"Layout written to {out_txt_path}")

if __name__ == "__main__":
    docx_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS 5 3 LANZAMIENTOS EDITORIALES COPIABLES\BONUS 5 3 LANZAMIENTOS EDITORIALES COPIABLES.docx"
    out_txt_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\bonus_5_layout_layout.txt"
    parse_docx_structure(docx_path, out_txt_path)
