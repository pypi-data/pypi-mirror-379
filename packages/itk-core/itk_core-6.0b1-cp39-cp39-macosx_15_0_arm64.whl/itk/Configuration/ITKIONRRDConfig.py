depends = ('ITKPyBase', 'ITKIOImageBase', )
templates = (  ('NrrdImageIOEnums', 'itk::NrrdImageIOEnums', 'itkNrrdImageIOEnums', False),
  ('NrrdImageIO', 'itk::NrrdImageIO', 'itkNrrdImageIO', True),
  ('NrrdImageIOFactory', 'itk::NrrdImageIOFactory', 'itkNrrdImageIOFactory', True),
)
factories = (("ImageIO","Nrrd"),)
