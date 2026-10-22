import type { Register } from 'claude-code'

// Contraste AA o mejor: ~10:1 sobre fondo oscuro, ~5:1 sobre blanco.
const VERDE_OSCURO = '#4ADE80'
const VERDE_CLARO = '#15803D'
const BURBUJA = '#2A2A2A' // gris de la burbuja de desktop en tema oscuro

export const register: Register = on => {
  on('ui.render', { component: 'UserMessage' }, async ($, e, next) => {
    // Solo tus prompts: notificaciones de tareas y mensajes de otras sesiones quedan igual.
    // En la terminal, ctrl+o (vista expandida) usa el dibujo normal. En desktop no hay ctrl+o:
    // ahí isExpanded siempre es true, así que no cuenta.
    const isTerminal = e.surface === 'terminal'
    if (e.props.task || e.props.from || (isTerminal && e.props.isExpanded)) return next(e)

    const theme = (await $.config.list()).find(row => row.key === 'theme')
    const color = String(theme?.value ?? '').includes('light') ? VERDE_CLARO : VERDE_OSCURO
    const { Box, Text } = $.ui.resolve(e)

    if (isTerminal) return <Text color={color} wrap="wrap">{`> ${e.props.text}`}</Text>

    // ponytail: imita la burbuja nativa de desktop (derecha, fondo gris); la API no deja recolorear la original.
    return (
      <Box flexDirection="row" justifyContent="flex-end" width="100%">
        <Box width="20%" flexShrink={0} />
        <Box backgroundColor={BURBUJA} borderStyle="round" borderColor={BURBUJA} paddingX={2} paddingY={1} flexShrink={1}>
          <Text color={color} wrap="wrap">{e.props.text}</Text>
        </Box>
      </Box>
    )
  })
}
