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
} else if (productName === 'rostro') {
  console.log('Post-build: Detected PRODUCT_NAME = "rostro". Overriding index.html with tu-como-rostro-de-marca.html...');
  const srcPath = path.join('dist', 'tu-como-rostro-de-marca.html');
  const destPath = path.join('dist', 'index.html');
  
  if (fs.existsSync(srcPath)) {
    fs.copyFileSync(srcPath, destPath);
    console.log('Post-build: Successfully copied tu-como-rostro-de-marca.html to index.html.');
  } else {
    console.error(`Post-build ERROR: Source file not found at ${srcPath}`);
  }
} else if (productName === 'radar') {
  console.log('Post-build: Detected PRODUCT_NAME = "radar". Overriding index.html with radar-de-tendencias-visuales.html...');
  const srcPath = path.join('dist', 'radar-de-tendencias-visuales.html');
  const destPath = path.join('dist', 'index.html');
  
  if (fs.existsSync(srcPath)) {
    fs.copyFileSync(srcPath, destPath);
    console.log('Post-build: Successfully copied radar-de-tendencias-visuales.html to index.html.');
  } else {
    console.error(`Post-build ERROR: Source file not found at ${srcPath}`);
  }
} else if (productName === 'casting') {
  console.log('Post-build: Detected PRODUCT_NAME = "casting". Overriding index.html with casting-infinito-ia.html...');
  const srcPath = path.join('dist', 'casting-infinito-ia.html');
  const destPath = path.join('dist', 'index.html');
  
  if (fs.existsSync(srcPath)) {
    fs.copyFileSync(srcPath, destPath);
    console.log('Post-build: Successfully copied casting-infinito-ia.html to index.html.');
  } else {
    console.error(`Post-build ERROR: Source file not found at ${srcPath}`);
  }
} else if (productName === 'lanzamientos') {
  console.log('Post-build: Detected PRODUCT_NAME = "lanzamientos". Overriding index.html with 3-lanzamientos-editoriales-copiables.html...');
  const srcPath = path.join('dist', '3-lanzamientos-editoriales-copiables.html');
  const destPath = path.join('dist', 'index.html');
  
  if (fs.existsSync(srcPath)) {
    fs.copyFileSync(srcPath, destPath);
    console.log('Post-build: Successfully copied 3-lanzamientos-editoriales-copiables.html to index.html.');
  } else {
    console.error(`Post-build ERROR: Source file not found at ${srcPath}`);
  }
} else {
  console.log('Post-build: Standard build, no overrides.');
}
