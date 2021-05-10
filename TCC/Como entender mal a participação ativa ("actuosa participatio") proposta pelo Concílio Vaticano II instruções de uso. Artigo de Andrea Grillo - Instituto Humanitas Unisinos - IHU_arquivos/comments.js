/**
 * Transforma resposta Flat da API para estrutura em árvore.

 * @author Marcelo Henrique <marcelohenrique180@asav.org.br>
 * 
 * @param array flatComments
 * @returns array
 */
function parseComments(flatComments) {

  // Completa parcialmente a funcao assignChilds para que findChilds e assignChild possuam os flatComments
  var assignAll = _.partial(assignChilds, flatComments)

  // Compõe uma função que atribui comentarios filhos a seus pais e mantem na raíz apenas os pais
  var parse = _.compose(assignAll(), keepOnlyParents())

  // usa essa função com os comentários
  return parse(flatComments)
}

function assignChilds(flatComments) {
  return _.map( function(comment) {
    return assignChild(flatComments, comment)
  });
}

function assignChild(flatComments, comment) {
  return _.assign({}, comment, comment.childs = assignChilds(flatComments)(findChilds(comment)(flatComments)))
}

function findChilds(comment) {
  return _.filter( function(child) {
    return comment.id === child.parent_id
 })
}

function keepOnlyParents() {
  return _.filter( function(comment) {
    return comment.parent_id === null
  })
}
