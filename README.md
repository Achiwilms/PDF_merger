# PDF_merger

A tool to merge your PDF files in the order you want.

## Environment 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package [pypdf](https://pypi.org/project/pypdf/).

```bash
pip install pypdf
```

## Usage
1. Clone or download this repository
2. Move to the repo's directory.
```bash
cd /path/to/directory/
```
4. Place the PDF files you want to merge to folder `pdf_original`
5. Run `merger.py`
```bash
python merger.py
```
6. Entet merging order, separating numbers with ","

Here's an exmaple, after running `merger.py`, the following message appears,
```bash
Find PDF files:
1. Wei Chuan Dragons.pdf
2. CTBC Brothers.pdf
3. Rakuten Monkeys.pdf
Enter the Merging Order (ex: 1, 3, 2, ...):
```
If you want to merge in the order `Wei Chuan Dragons.pdf`, `Rakuten Monkeys.pdf`, `CTBC Brothers.pdf`,  just enter
```bash
1, 3, 2
```
7. You can find the merged PDF file in the folder `pdf_merged` 


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)