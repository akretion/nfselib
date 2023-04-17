<p align="center">
<a href="https://codecov.io/gh/akretion/nfselib" > 
 <img src="https://codecov.io/gh/akretion/nfselib/branch/nfselib-xsdata/graph/badge.svg?token=Xg2OpCNM5N"/> 
</a>
<a href="https://pypi.org/project/nfelib/"><img alt="PyPI" src="https://img.shields.io/pypi/v/nfselib"></a>
</p>

# nfselib: a lib Python limpa que suporta a NFS-e de mais de 450 cidades do Brasil

A nfelib usa os famosos schemas do projeto open source [UNINFE](https://unimake.com.br/uninfe/) junto com o poder do [xsdata](https://xsdata.readthedocs.io/en/latest/) para tornar facil a importação e geração em Python dos arquivos XML das NFS-e de mais de 450 cidades do Brasil.

Existe tambem agora a NFS-e com o padrão da Receita Federal, esse esta pela [nfelib](https://github.com/akretion/nfelib), uma lib mais générica sem ligação com o UNINFE e que suporta todos padrões de notas fiscais nacionais.


## Como atualizar os schemas a partir do repo svn do UNINFE:

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
]()
