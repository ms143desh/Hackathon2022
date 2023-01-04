package io.peerislands.hackathon2022intellijplugin;

import org.jetbrains.annotations.NotNull;

import com.intellij.openapi.project.Project;
import com.intellij.openapi.wm.ToolWindow;
import com.intellij.openapi.wm.ToolWindowFactory;
import com.intellij.ui.content.Content;
import com.intellij.ui.content.ContentFactory;

public class DemoToolWindowFactory implements ToolWindowFactory {
    @Override
    public void createToolWindowContent(@NotNull final Project project, @NotNull final ToolWindow toolWindow) {
        DemoToolWindow demoToolWindow = new DemoToolWindow(toolWindow);
        ContentFactory contentFactory = ContentFactory.SERVICE.getInstance();
        Content content = contentFactory.createContent(demoToolWindow.getContent(), "", false);
        toolWindow.getContentManager().addContent(content);
    }
}
