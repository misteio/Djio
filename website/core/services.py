import os
import datetime
import random
from django.conf import settings
from django.http import HttpResponse
from PIL import Image
from resizeimage import resizeimage
from django.core.files.storage import FileSystemStorage


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'])
UPLOAD_FOLDER = '/home/miste/Documents/Gits/Djio/media/'


def check_allowed_file(file):
    if file and allowed_file(file.filename):
        return True
    else:
        return False


def ckupload_service(request):
    """CKEditor file upload"""
    error = ''
    url = ''
    callback = request.GET["CKEditorFuncNum"]
    if request.method == 'POST' and 'upload' in request.FILES:
        fileobj = request.FILES['upload']
        fname, fext = os.path.splitext(fileobj.name)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        filepath = os.path.join(UPLOAD_FOLDER, rnd_name)

        fs = FileSystemStorage()
        filename = fs.save(filepath, fileobj)
        uploaded_file_url = fs.url(filepath)


        original_url = 'http://localhost:8000/static/' + 'test.jpg'
        #original_url = '/static' + url_for('static', filename='%s/%s' % ('images', rnd_name))
        url = original_url

        # Here we create a cropped thumbnail
        with open(filepath, 'r+b') as f:
            with Image.open(f) as image:
                if image.width > 99:
                    cover = resizeimage.resize_cover(image, [100, 100])
                    thumbnail_path = os.path.join(UPLOAD_FOLDER, 'small_' + rnd_name)
                    cover.save(thumbnail_path, image.format)

                if image.width > 1199:
                    web = resizeimage.resize_width(image, 1200)
                    web_path = os.path.join(UPLOAD_FOLDER, 'web_' + rnd_name)
                    web.save(web_path, image.format)

    else:
        error = 'post error'

    res = """<script type="text/javascript">
             window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
             </script>""" % (callback, url, error)
    return HttpResponse(res)

    #response = make_response(res)
    #response.headers["Content-Type"] = "text/html"

    #return response


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))