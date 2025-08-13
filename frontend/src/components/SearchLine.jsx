import { Input, ConfigProvider } from "antd"
const { Search } = Input

const SearchLine = ({ className }) => (
  <ConfigProvider
    theme={{
      components: {
        Button: {
          colorPrimary: "#7259F3",
          colorPrimaryHover: "#9691FF",
          colorPrimaryActive: "#75D4EC",
        },
      },
    }}
  >
    <Search
      className={className}
      placeholder='Введите запрос...'
      enterButton='Найти'
      size='large'
    />
  </ConfigProvider>
)

export default SearchLine
