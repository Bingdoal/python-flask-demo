import sys
import traceback

from flask_restful import abort


def abort_msg(e):
    error_class = e.__class__.__name__  # 引發錯誤的 class
    detail = e.args[0]  # 得到詳細的訊息
    cl, exc, tb = sys.exc_info()  # 得到錯誤的完整資訊 Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1]  # 取得最後一行的錯誤訊息
    fileName = lastCallStack[0]  # 錯誤的檔案位置名稱
    lineNum = lastCallStack[1]  # 錯誤行數
    funcName = lastCallStack[2]  # function 名稱
    errMsg = "Exception raise in file: {}, line {}, in {}: [{}] {}. Please contact the member who is the person in " \
             "charge of project!".format(
        fileName, lineNum, funcName, error_class, detail)
    abort(500, errMsg)
