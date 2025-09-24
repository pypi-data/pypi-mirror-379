

def get_excel_file_from_link(ctx, sharepoint_link):

    # get the folder link from the file link
    sharepoint_folder_link = sharepoint_link.rsplit('/', maxsplit=1)[0]
    
    # get sharepoint folder
    libraryRoot = ctx.web.get_folder_by_server_relative_path(sharepoint_folder_link)
    ctx.load(libraryRoot)
    ctx.execute_query()

    # get files in folder
    files_in_folder = libraryRoot.files
    ctx.load(files_in_folder)
    ctx.execute_query()

    # debug
    # print(f'{files_in_folder = }')

    # with the condition that there is only one file
    # excel_file = files_in_folder[0]

    for file in files_in_folder:
        files_url = file.properties['ServerRelativeUrl']
        if files_url == sharepoint_link:
            return file

    raise Exception('[ERROR]: Cannot find the specified file!')
    # return excel_file