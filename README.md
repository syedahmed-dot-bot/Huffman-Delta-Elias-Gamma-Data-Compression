# Huffman + Delta + Elias Gamma Compression

This project implements a custom **lossless compression algorithm** that combines three classical techniques:

- **Delta Encoding**
- **Elias Gamma Encoding**
- **Huffman Coding**

The goal is to efficiently compress sequences of integers — particularly useful for time-series data or structured representations.

---

## How It Works

### 1. **Delta Encoding**
Reduces redundancy by encoding the *difference* between consecutive numbers.

### 2. **Elias Gamma Encoding**
Encodes each non-negative integer using a variable-length, prefix-free binary format.  
It is especially efficient for small numbers (like deltas).


---

### 3. **Huffman Coding**
Compresses the Elias Gamma bitstream further by assigning shorter binary codes to more frequent patterns (bit chunks).

---

## 🔄 Compression Flow

1. Flatten the input list of integers
2. Apply delta encoding
3. Convert delta values to Elias Gamma codes
4. Split the Elias bitstream into fixed-size chunks (e.g., 9 bits)
5. Build a Huffman tree over chunk frequencies
6. Encode the chunk list using Huffman
7. Store compressed bitstream and metadata (if needed)

---

## 🔄 Decompression Flow

1. Decode Huffman-encoded bitstream into Elias Gamma chunks
2. Decode Elias Gamma back into integer deltas
3. Apply inverse delta to reconstruct original list

---

## 📊 Compression Stats (Sample Output)

| Metric              | Value         |
|---------------------|---------------|
| Lossless            | ✅ Yes  
| Compression Ratio   | ~5.0× (for short list)  
| Compression %       | ~79.17%  
| Input               | `[100, 101, 104]`

---

## 📁 File Structure

- `compressor.py` — Contains all compression and decompression functions
- `main.py` — Sample run and test of pipeline
- `README.md` — This file

---

##  Limitations

- Elias Gamma only supports non-negative values → delta values must be offset
- Fixed chunking (e.g., 9-bit) can misalign Elias Gamma codes if not handled carefully
- Not optimal for large-scale data— better alternatives: Bitpacking or Golomb coding

---

##  Good For:

- Learning and experimenting with classic compression techniques
- Understanding data encoding theory
- Building a custom lossless compressor from scratch

---

## 🚀 Future Improvements

- Replace Elias Gamma with Elias Delta or Golomb encoding
- Use Huffman on Elias-symbols, not raw bits
- Add file I/O and custom compression format
- Add streaming/block-based support

---

## 👨‍💻 Author

Developed by **Ahmed Hussain Syed** as part of a deeper exploration into AI-focused data compression challenges.

