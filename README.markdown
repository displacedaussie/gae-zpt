First of all I'll explain how to use ZPT in a normal project. From there I'll show you specifically how to get it working with Google App Engine.

**Install zope.pagetemplate**

    # easy_install zope.pagetemplate

**In your python view code, add something like this**

    from zope.pagetemplate.pagetemplatefile import PageTemplateFile

    my_pt = PageTemplateFile('mytemplate.pt') 
    context = {'row': ['apple', 'banana', 'carrot'], 'foo':'bar'}
    print my_pt.pt_render(namespace=context)

**In your template (`mytemplate.pt`)**

    <html> 
      <body> 
        <h1>Hello World</h1>
        <div tal:condition="python:foo == 'bar'"> 
          <ul> 
            <li tal:repeat="item rows" tal:content="item" /> 
          </ul> 
        </div>
      </body> 
    </html>

What this basically means is that you'll need to do the following:

 - Make sure you can install zope.pagetemplate
 - Create a .pt file
 - In your view code, name a template and then render it with the given context

**Google App Engine**

In GAE you're able to use (almost) any code you like, but you have to provide it with your application. To make use of ZPT you'll need to get copies of the zope.pagetemplate package and anything it depends on. I can tell you that when you do an `# easy_install zope.pagetemplate` you end up with the following packages:

 - zope.pagetemplate
 - zope.i18nmessageid
 - zope.interface
 - zope.tal
 - zope.tales

It's highly likely that you can trim these down and remove the code that you don't actually need, but I'll leave this as an exercise for you.

Once you have a copy of each of the above packages, put the code from each package into a "zope" directory that you'll be able to include with your GAE application. This will allow you to import everything the standard way.

Assuming you've got to this point, the next step is to create the template as above, put the view code into the appropriate RequestHandler, and then write the rendered output at the end of each request.

I've created a basic GAE application that does this and you can [download it][1] from GitHub.

For any existing (or new) projects you have, just take the 'zope' directory from the example application and use it as described above. 

This example application will be expanded and is deployed [here][2].

  [1]: http://github.com/displacedaussie/gae-zpt
  [2]: http://gae-zpt.appspot.com