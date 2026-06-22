import fs from 'fs';
import path from 'path';

const productName = process.env.PRODUCT_NAME;

if (productName === 'prenda') {
  console.log('Post-build: Detected PRODUCT_NAME = "prenda". Overriding index.html with de-prenda-a-campana.html...');
  const srcPath = path.join('dist', 'de-prenda-a-campana.html');
  const destPath = path.join('dist', 'index.html');
  
  if (fs.existsSync(srcPath)) {
    fs.copyFileSync(srcPath, destPath);
    console.log('Post-build: Successfully copied de-prenda-a-campana.html to index.html.');
  } else {
    console.error(`Post-build ERROR: Source file not found at ${srcPath}`);
  }
} else {
  console.log('Post-build: Standard build, no overrides.');
}
