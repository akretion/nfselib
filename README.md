# UNINFE - Projeto Documentos Fiscais Eletrônicos - NFSe git mirror
mirror of http://sourceforge.net/p/uninfe/code 


How to update:

```
git svn clone http://svn.code.sf.net/p/uninfe/code --no-metadata --stdlayout uninfe-git
cd uninfe-git
git filter-branch --subdirectory-filter fontes/NFe.Components.Wsdl/NFse
git add ak https://github.com/akretion/nfselib.git
git fetch ak soap:soap
git checkout soap
```

then use `git cherry-pick` to add the missing WSDL or Webservice.xml commits from the master branch to the soap branch
