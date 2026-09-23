'use strict';
const fs = require('node:fs');
const path = require('node:path');
const { createHash } = require('node:crypto');
const root = path.resolve(__dirname, '..');
const directory = path.join(root, 'media');
const lines = fs.readFileSync(path.join(directory, 'SHA256SUMS'), 'utf8').trim().split('\n');
const inventory = new Set();
for (const line of lines) {
  const match = /^([a-f0-9]{64})  ([a-z0-9-]+\.(?:png|gif))$/.exec(line);
  if (!match || inventory.has(match[2])) throw new Error('Invalid or duplicate checksum entry');
  const [, expected, name] = match;
  inventory.add(name);
  const file = path.join(directory, name);
  if (!fs.lstatSync(file).isFile()) throw new Error(`Regular file required: ${name}`);
  const bytes = fs.readFileSync(file);
  if (createHash('sha256').update(bytes).digest('hex') !== expected) throw new Error(`Checksum mismatch: ${name}`);
  if (name.endsWith('.png')) {
    if (bytes.length < 33 || bytes.subarray(0, 8).toString('hex') !== '89504e470d0a1a0a' || bytes.subarray(12,16).toString() !== 'IHDR') throw new Error(`Invalid PNG: ${name}`);
    const width = bytes.readUInt32BE(16), height = bytes.readUInt32BE(20);
    const normalized = name.startsWith('jetbrains-marketplace-');
    const rawJetbrains = name.startsWith('jetbrains-') && !normalized;
    if (rawJetbrains ? width < 1000 || height < 700 : width !== 1280 || height !== (normalized ? 800 : 720)) throw new Error(`Invalid dimensions ${width}x${height}: ${name}`);
  } else if (!/^GIF8[79]a$/.test(bytes.subarray(0,6).toString()) || bytes.readUInt16LE(6) !== 960 || bytes.readUInt16LE(8) !== 540) throw new Error(`Invalid archival GIF: ${name}`);
}
const images = fs.readdirSync(directory).filter((name) => /\.(png|gif)$/.test(name));
if (images.length !== inventory.size || images.some((name) => !inventory.has(name))) throw new Error('Checksum inventory incomplete');
if (images.filter((name) => name.endsWith('.png')).length !== 33 || images.filter((name) => name.endsWith('.gif')).length !== 2) throw new Error('Release inventory changed; explicit review required');
console.log(`Media integrity passed: ${inventory.size} hashes, complete inventory and image dimensions.`);
