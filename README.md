<p align="center">
<a href="https://codecov.io/gh/akretion/nfselib" > 
 <img src="https://codecov.io/gh/akretion/nfselib/branch/nfselib-xsdata/graph/badge.svg?token=Xg2OpCNM5N"/> 
</a>
<a href="https://pypi.org/project/nfelib/"><img alt="PyPI" src="https://img.shields.io/pypi/v/nfselib"></a>
</p>

# nfselib: a lib Python limpa que suporta a NFS-e de mais de 450 cidades do Brasil

A nfelib usa os famosos schemas do projeto open source [UNINFE](https://unimake.com.br/uninfe/) junto com o poder do [xsdata](https://xsdata.readthedocs.io/en/latest/) para tornar facil a importação e geração dos arquivos XML das NFS-e de mais de 450 cidades do Brasil no ambiente Python.

Existe tambem agora a NFS-e com o padrão da Receita Federal, esse esta suportado pela [nfelib](https://github.com/akretion/nfelib), uma lib mais générica sem ligação com o UNINFE e que suporta todos padrões de notas fiscais nacionais.


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

Por fim criar um PR no Github para integrar essas atualizações.
