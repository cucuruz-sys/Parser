from Parser import downloadImages
def main():
    # list = fetch_items(5)
    # for item in list:
    item = "Диван"
    downloadImages(item, 5, 'D:/parser/' + item)
if __name__ == "__main__":
    main()
