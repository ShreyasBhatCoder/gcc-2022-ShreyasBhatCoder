def solution_2(files):
  files = [i for i in files]
  res = {files.count(x) for x in set(files)}
  return sum(res)
