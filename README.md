# nfselib: a lib for the the legacy NFS-e in Brazil


How to update the schemas from the UNINFE svn repo:

```
git svn clone http://svn.code.sf.net/p/uninfe/code --no-metadata --stdlayout uninfe-git
cd uninfe-git
git filter-branch --subdirectory-filter fontes/NFe.Components.Wsdl/NFse
git add ak git@github.com:akretion/nfselib.git
git fetch ak nfselib-xsdata:nfselib-xsdata
git checkout nfselib-xsdata
git rebase master
git push ak nfselib-xsdata:nfselib-xsdata-tmp
```

And finally create a merge request in Github against the nfeslib-xsdata branch.

Note: we could also use `git cherry-pick` to add the missing WSDL or Webservice.xml commits
