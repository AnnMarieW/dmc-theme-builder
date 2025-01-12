
# Dash Mantine Components Theme Builder

### Customize Your Dash App's Theme  

Mantine comes with a great default theme that works in both light and dark modes. This theme is defined in a **[Theme Object](https://www.dash-mantine-components.com/theme-object)**, which is a dictionary of settings you can change to suit your needs.  

You can customize things like colors, border radius, spacing and breakpoints, fonts and text styles, component defaults and more! To make changes, simply create a new theme dictionary with your settings. Mantine will automatically merge it with the default theme, so you only need to include what you want to change.  

For a full list of options, check out the **[Theme Object documentation](https://www.dash-mantine-components.com/theme-object)**.  

---

### About This App  

This app dynamically customizes some key aspects of Mantine’s theme.  Use it to adjust:
- The **primary accent color**  
- The **default border radius**  
- The **shadow style** applied to card components  
- The **color scheme** (light or dark mode)  

Explore the app live: **[DMC Theme Builder on Pycafe](https://py.cafe/app/dash.mantine.components/dash-mantine-theme-builder)**  

![DMC Theme Builder Screenshot](https://github.com/user-attachments/assets/afeae598-aa4a-424f-88ee-5ef0861a0d8d)  

---

### How to Use Your Custom Theme  

Once you've customized your theme, click the **"Copy theme code"** button in the app. This will generate the code for the theme you've configured.  Apply theme to your Dash app like this:  

```python
import dash_mantine_components as dmc

theme = {
    "primaryColor": "teal",
    "defaultRadius": "xl",
    "components": {
        "Card": {
            "defaultProps": {
                "shadow": "xl"
            }
        }
    }
}

app.layout = dmc.MantineProvider(
    theme=theme,
    children=[]  # Add your app layout here
)
```  

This approach ensures a consistent, customized design across all components in your Dash app.  

---

### Learn More  

For further details and advanced theming techniques, visit the Dash Mantine Components documentation:  

- **[Mantine API Overview](https://www.dash-mantine-components.com/mantine-api)**: High-level overview of Mantine's styling and theming options.  
- **[Theme Object](https://www.dash-mantine-components.com/theme-object)**: In-depth guide to customizing the default theme.  
- **[Styles API](https://www.dash-mantine-components.com/styles-api)**: How to override styles globally or at the component level.  
