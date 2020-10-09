erpbrasil-edoc-gen-download-schema -n ginfes -v v3.01 -u https://itajuba.ginfes.com.br/nfseweb/download/schemas_v301Abrasf.zip
erpbrasil-edoc-gen-generate-python -m nfse -n ginfes -v v3.01 -i "servico_enviar_lote_rps_resposta_v03|servico_consultar_situacao_lote_rps_resposta_v03|servico_consultar_lote_rps_resposta_v03|servico_enviar_lote_rps_envio_v03|servico_consultar_situacao_lote_rps_envio_v03|servico_consultar_lote_rps_envio_v03|servico_cancelar_nfse_envio_v03|servico_consultar_nfse_rps_envio_v03|cabecalho_v03|servico_consultar_nfse_resposta_v03|servico_cancelar_nfse_resposta_v03" -d .
# O servico_enviar_lote_rps_envio_v03 foi necessário pois a classe EnviarLoteRpsEnvio
# não estava no arquivo de retorno.
