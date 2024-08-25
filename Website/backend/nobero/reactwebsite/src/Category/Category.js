import "./Category.css"
import Input from "../../components/Input";



function Category ({handleChange}){
    return (
        <div>
            <h2 className="sidebar-title">Category</h2>
           <div>
                 <label className="sidebar-label-container">
                    <input onChange={handleChange} type="radio" value="" name="test"/>
                    <span className="checkmark">All</span>
                </label>
                <Input handleChange={handleChange} 
                value="Men" title="Men"/>
                 <Input handleChange={handleChange} 
                value="Women" title="Women"/>
                 <Input handleChange={handleChange} 
                value="Joggers" title="Joggers"/>
                <Input handleChange={handleChange} value="Classic T-Shirts"
                title="Classic T-Shirts"/>
                <Input handleChange={handleChange} value="Fashion Joggers"
                title="Fashion Joggers"/>
                



           </div> 
        </div>
    )
}