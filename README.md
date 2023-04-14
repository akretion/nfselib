# UNINFE - Projeto Documentos Fiscais Eletrônicos - NFSe git mirror
mirror of http://sourceforge.net/p/uninfe/code 


How to update from UNINFE:

```
git svn clone http://svn.code.sf.net/p/uninfe/code --no-metadata --stdlayout uninfe-git
cd uninfe-git
git filter-branch --subdirectory-filter fontes/NFe.Components.Wsdl/NFse
git add ak git@github.com:akretion/nfselib.git
git fetch ak nfselib-ng:nfselib-ng
git checkout nfselib-ng
git rebase master
git push ak nfselib-ng:nfselib-ng-tmp
```

Note: we could also use `git cherry-pick` to add the missing WSDL or Webservice.xml commits
