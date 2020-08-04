meta:
  id: packed
  application: Scrapland
  file-extension: packed
  endian: le
  xref: http://wiki.xentax.com/index.php/Scrapland_PACKED
  license: MIT
  encoding: latin1

seq:
  - id: magic
    contents: BFPK
    doc: File Magic
  - id: version
    type: u2
    size: 4
    doc: Second File Magic
  - id: num_files
    type: u4
    doc: Number of files
  - id: files
    type: file_entry
    repeat: expr
    repeat-expr: num_files
    doc: Directory entry for each file

types:
  file_entry:
    seq:
      - id: path_len
        type: u4
        doc: Length of file path
      - id: path
        type: str
        size: path_len
        doc: File path
      - id: size
        type: u4
        doc: File size
      - id: offset
        type: u4
        doc: Absoulte File offset
    instances:
      data:
        pos: offset
        size: size