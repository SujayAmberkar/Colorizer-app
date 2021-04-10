import Algorithmia,os

img = "https://www.clickonf5.org/wp-content/uploads/2011/04/charlie-chaplin-doodle-1.jpg"
input = {
  "image": img
}
client = Algorithmia.client('sim7jOc/vjd9Mbat8RF47TFwnk61')
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.14')
algo.set_options(timeout=300) # optional
img_file=algo.pipe(input).result["output"]
print(img_file)
# client.dir("data://.my/foo").create()
client.file(path)
foo = client.dir("data://.my/foo")
foo.file(img_file).putFile("/path/to/myfile")






