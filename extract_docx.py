import os
import zipfile
import xml.etree.ElementTree as ET

def extract_docx(docx_path, out_img_dir, out_text_path):
    print(f"Opening {docx_path}...")
    if not os.path.exists(docx_path):
        print(f"Error: {docx_path} does not exist.")
        return
        
    os.makedirs(out_img_dir, exist_ok=True)
    
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        # Extract images
        media_files = [f for f in zip_ref.namelist() if f.startswith('word/media/')]
        print(f"Found {len(media_files)} media files in DOCX.")
        
        for media_file in media_files:
            base_name = os.path.basename(media_file)
            dest_path = os.path.join(out_img_dir, base_name)
            with open(dest_path, 'wb') as f_out:
                f_out.write(zip_ref.read(media_file))
            print(f"Extracted image: {base_name}")
            
        # Extract text from document.xml
        try:
            doc_xml = zip_ref.read('word/document.xml')
            root = ET.fromstring(doc_xml)
            
            # Namespaces
            ns = {
                'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
            }
            
            paragraphs = []
            for para in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                texts = []
                for run in para.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                    if run.text:
                        texts.append(run.text)
                para_text = "".join(texts)
                paragraphs.append(para_text)
                
            print(f"Extracted {len(paragraphs)} paragraphs of text.")
            
            with open(out_text_path, 'w', encoding='utf-8') as f_txt:
                for p in paragraphs:
                    f_txt.write(p + "\n")
            print(f"Text written to {out_text_path}")
            
        except Exception as e:
            print(f"Error extracting text: {e}")

if __name__ == "__main__":
    docx_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\PRODUCTO PRINCIPAL  DE PRENDA A CAMPAÑA\DE PRENDA A CAMPAÑA.docx"
    out_img_dir = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\public\media\de_prenda_a_campana"
    out_text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\DE_PRENDA_A_CAMPANA_TEXT.txt"
    extract_docx(docx_path, out_img_dir, out_text_path)
